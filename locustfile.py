from locust import HttpUser, task, between
import logging

# Set up logging
logging.basicConfig(filename='locust_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class ImageryLayerUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def get_imagery_layer(self):
        url = "https://gis.earthdata.nasa.gov/maps/rest/services/EIC/heatmax_median_multivariate_annual/ImageServer"
        params = {
            'geometry': '{"spatialReference":{"wkid":4326},"x":-103.3665440972982,"y":0.995054807838955}',
            'geometryType': '"point"',
            'mosaicRule': '{"ascending":True,"multidimensionalDefinition":[{"variableName":"heatmax_ssp126","dimensionName":"StdTime","values":[[-628560000000,249868800000]],"isSlice":False},{"variableName":"heatmax_ssp245","dimensionName":"StdTime","values":[[-628560000000,249868800000]],"isSlice":False}]}',
            'returnFirstValueOnly': 'False',
            'interpolation': 'RSP_NearestNeighbor',
            'f': 'json'
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
