from rest_framework.views import APIView
from projectboard.models import Boardmodel, TaskModel
from projectboard.serializer import ProjectSerrializer, TaskSerializer
from rest_framework import status
from rest_framework.response import Response

from teams.models import team

# Create your views here.
class ProjectBoardBase(APIView):
    """ 
    A project board is a unit of delivery for a project. Each board will have a set of tasks assigned to a user.
    """

    def post(self, request, format=None):

        if 'user_id' in request.data:
          id = self.add_task(request)
          return Response({"id":id}, status=status.HTTP_201_CREATED)
        
        elif len(request.data) == 3 :
            id = self.create_board(request)
            return Response({"id":id}, status=status.HTTP_201_CREATED)
        
        elif len(request.data) == 2 :
            id = self.update_task_status(request.data['id'],request.data['status'])
            return Response("Updated Successfully")
        
        elif len(request.data) == 1:
          boards = self.list_boards(request.data['id'])
          return Response(boards)

        else:
          return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, format=None):
        if pk is not None:
          self.close_board(pk)
          return Response("Updated Successfully")
        else:
          Response(status=status.HTTP_400_BAD_REQUEST)
    

    # create a board
    def create_board(self, request, format=None):
        """
        :param request: A json string with the board details.
        {
            "name" : "<board_name>",
            "description" : "<description>",
            "team_id" : "<team id>"
            "creation_time" : "<date:time when board was created>"
        }
        :return: A json string with the response {"id" : "<board_id>"}

        Constraint:
         * board name must be unique for a team
         * board name can be max 64 characters
         * description can be max 128 characters
        """
        serializer = ProjectSerrializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data.get('id')


    # close a board
    def close_board(self, pk):
        """
        :param request: A json string with the user details
        {
          "id" : "<board_id>"
        }

        :return:

        Constraint:
          * Set the board status to CLOSED and record the end_time date:time
          * You can only close boards with all tasks marked as COMPLETE
        """
        teamid = Boardmodel.objects.filter(id=pk).values('team')
        for id in teamid:
          statuses = TaskModel.objects.filter(user_id=id['team']).values('status')
        count = 0
        for status in statuses:
          if status['status'] == 'closed':
            count+=1
        if count == len(statuses):
          Boardmodel.objects.filter(id=pk).update(status='closed')
        
       
    # add task to board
    def add_task(self, request):
        """
        :param request: A json string with the task details. Task is assigned to a user_id who works on the task
        {
            "title" : "<board_name>",
            "description" : "<description>",
            "user_id" : "<team id>"
            "creation_time" : "<date:time when task was created>"
        }
        :return: A json string with the response {"id" : "<task_id>"}

        Constraint:
         * task title must be unique for a board
         * title name can be max 64 characters
         * description can be max 128 characters

        Constraints:
        * Can only add task to an OPEN board
        """
        statusss = Boardmodel.objects.filter(team=request.data['user_id']).values('status')
        count = 0
        for status in statusss:
          if status['status'] == 'open':
            count+=1
        if count == len(statusss):
          serializer = TaskSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return serializer.data.get('id')

    # update the status of a task
    def update_task_status(self, pk, status):
        """
        :param request: A json string with the user details
        {
            "id" : "<task_id>",
            "status" : "OPEN | IN_PROGRESS | COMPLETE"
        }
        """
        TaskModel.objects.filter(id=pk).update(status=status)

    # list all open boards for a team
    def list_boards(self, pk):
        """
        :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<board_id>",
            "name" : "<board_name>"
          }
        ]
        """
        query=Boardmodel.objects.filter(team=pk).values('id','name').all()
        return query

    def export_board(self, request: str) -> str:
        """
        Export a board in the out folder. The output will be a txt file.
        We want you to be creative. Output a presentable view of the board and its tasks with the available data.
        :param request:
        {
          "id" : "<board_id>"
        }
        :return:
        {
          "out_file" : "<name of the file created>"
        }
        """
        pass
