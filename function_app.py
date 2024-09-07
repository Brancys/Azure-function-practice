import azure.functions as func
import logging
import Service.queue_samples_hello_world as colas
from azure.identity import DefaultAzureCredential

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    queue = req.params.get('queue')  

    if not name or not queue:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sample = colas.QueueHelloWorldSamples()
            sample.create_client_with_connection_string()

            name = req_body.get('name')
            queue = req_body.get('queue')  
            sample.queue_and_messages_example(queue)  

    if name and queue:
        return func.HttpResponse(f"Hello, {name}. Queue '{queue}' created successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name and queue in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.function_name(name="DeletedQueue")
@app.route(route="queue/delete", auth_level=func.AuthLevel.ANONYMOUS, methods=['POST'])
def delete_queue(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    queue = req.params.get('queue')  

    if not name or not queue:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sample = colas.QueueHelloWorldSamples()
            name = req_body.get('name')
            queue = req_body.get('queue')  
            sample.delete_queue_do(queue)  
    if name and queue:
        return func.HttpResponse(f"Hello, {name}. Queue '{queue}' deleted successfully.")
    else:
        return func.HttpResponse(
             "This delete queue function executed successfully. Pass a name and queue in the query string or in the request body for a personalized response.",
             status_code=200
        )
