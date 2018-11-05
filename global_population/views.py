from rest_framework import generics
from rest_framework.views import Response, status

from global_population.utils import validate_query_data
from .population_evaluation import get_population


class GetPopulationView(generics.RetrieveAPIView):

    # serializer_class = PopulationSerializer

    def get(self, request, *args, **kwargs):

        query_latitude = request.query_params.get('latitude')
        query_longitude = request.query_params.get('longitude')
        query_radius = request.query_params.get('radius')
        validate_context = validate_query_data(query_latitude, query_longitude, query_radius)

        if validate_context['status']:
            query_population = get_population(float(query_latitude), float(query_longitude), float(query_radius))

            # Population.objects.create(longitude=query_longitude, latitude=query_latitude, radius=query_radius,
            #                           population=query_population)
            response_context = {
                'longitude': float(query_longitude),
                'latitude': float(query_latitude),
                'radius': float(query_radius),
                'population': query_population
            }
            # return Population.objects.last()
            return Response(response_context)

        return Response(validate_context['error'], status=status.HTTP_400_BAD_REQUEST)
