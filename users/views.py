from rest_framework.views import APIView
from users.models import user
from teams.models import team
from rest_framework.response import Response
from users.serializers import UserSerializer, UserPatchSerializer, UserGETSerializer
from rest_framework import status

# Create your views here.

class UserBase(APIView):
    """
    Base interface implementation for API's to manage users.
    """
    def post(self, request, format=None):
        
        Response = self.create_user(request)
        return Response
      
    def get(self, request, pk=None):
        
        if 'id' in request.data:
          response = self.get_user_teams(request.data['id'])
        elif pk is None:
          response = self.list_users()
        else:
          response = self.describe_user(pk)
        return response

    def patch(self, request, pk=None, format=None):
        response = self.update_user(request, pk, format)
        return response



    # create a user
    def create_user(self, request):
        """
        :param request: A json string with the user details
        {
          "name" : "<user_name>",
          "display_name" : "<display name>"
          "description" : "<some description>",
        }
        :return: A json string with the response {"id" : "<user_id>"}

        Constraint:
            * user name must be unique
            * name can be max 64 characters
            * display name can be max 64 characters
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id":serializer.data.get('id')}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # list all users
    def list_users(self):
        """
        :return: A json list with the response
        [
          {
            "name" : "<user_name>",
            "display_name" : "<display name>",
            "creation_time" : "<some date:time format>"
          }
        ]
        
        or

        :param request: A json string with the user details
        {
          "id" : "<user_id>"
        }

        :return: A json string with the response

        {
          "name" : "<user_name>",
          "description" : "<some description>",
          "creation_time" : "<some date:time format>"
        }

        """
        usser = user.objects.all()
        serializer = UserGETSerializer(usser, many=True)
        return Response(serializer.data)


     # describe user
    def describe_user(self, pk):
        """
        :param request: A json string with the user details
        {
          "id" : "<user_id>"
        }

        :return: A json string with the response

        {
          "name" : "<user_name>",
          "description" : "<some description>",
          "creation_time" : "<some date:time format>"
        }

        """
        uuser = user.objects.get(id=pk)
        serializer = UserGETSerializer(uuser)
        return Response(serializer.data)

    # update user
    def update_user(self, request, pk=None) -> str:
        """
        :param request: A json string with the user details
        {
          "id" : "<user_id>",
          "user" : {
            "name" : "<user_name>",
            "display_name" : "<display name>"
          }
        }

        :return:

        Constraint:
            * user name cannot be updated
            * name can be max 64 characters
            * display name can be max 128 characters
        """
        usser = user.objects.get(id=pk)
        serializer = UserPatchSerializer(usser, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully Updated")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_user_teams(self,pk=None):
        """
        :param request:
        {
          "id" : "<user_id>"
        }

        :return: A json list with the response.
        [
          {
            "name" : "<team_name>",
            "description" : "<some description>",
            "creation_time" : "<some date:time format>"
          }
        ]
        """
        
