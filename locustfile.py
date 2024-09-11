from locust import HttpUser, task, between
import logging

# Set up logging
logging.basicConfig(filename='locust_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class ImageryLayerUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def get_imagery_layer(self):
        url = "https://civsci.esrigc.com/image/rest/services/heatmax_median_multivariate_annual_cw/ImageServer"
        params = {
            'geometry': 'GEOMETRY',
            'geometryType': 'GEOMETRY_TYPE',
            'mosaicRule': 'MOSAIC_RULE',
            'returnFirstValueOnly': 'RETURN_FIRST_VALUE',
            'interpolation': 'INTERPOLATION'
        }
        with self.client.get(url, params=params, catch_response=True) as response:
            elapsed_time = response.elapsed.total_seconds()
            logging.info(f"GET Request URL: {response.url}")
            logging.info(f"Elapsed Time: {elapsed_time} seconds")
            logging.info(f"Status Code: {response.status_code}")
            logging.info(f"Response Headers: {response.headers}")
            logging.info(f"Response Content: {response.text[:500]}")  # Log first 500 characters of the response content
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status code {response.status_code}")

    @task
    def post_imagery_layer(self):
        url = "https://civsci.esrigc.com/image/rest/services/heatmax_median_multivariate_annual_cw/ImageServer"
        data = {
            'geometry': 'GEOMETRY',
            'geometryType': 'GEOMETRY_TYPE',
            'mosaicRule': 'MOSAIC_RULE',
            'returnFirstValueOnly': 'RETURN_FIRST_VALUE',
            'interpolation': 'INTERPOLATION'
        }
        with self.client.post(url, data=data, catch_response=True) as response:
            elapsed_time = response.elapsed.total_seconds()
            logging.info(f"POST Request URL: {response.url}")
            logging.info(f"Elapsed Time: {elapsed_time} seconds")
            logging.info(f"Status Code: {response.status_code}")
            logging.info(f"Response Headers: {response.headers}")
            logging.info(f"Response Content: {response.text[:500]}")  # Log first 500 characters of the response content
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status code {response.status_code}")