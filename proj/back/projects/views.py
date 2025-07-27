from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import Project, Feature, Challenge, projimage, Outcome
from .serializers import ProjectSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
   
    

class ProjectCreateView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        features_input = request.data.get('features', '')
        challenges_input = request.data.get('challenges', '')
        projimage_input = request.FILES.getlist('images')
        outcomes_input = request.data.get('outcomes', '')

        # Clean data before validation
        mutable_data = request.data.copy()
        mutable_data.pop('features', None)
        mutable_data.pop('challenges', None)
        mutable_data.pop('images', None)
        mutable_data.pop('outcomes', None)

        serializer = ProjectSerializer(data=mutable_data)

        if serializer.is_valid():
            project = serializer.save()

            # Features
            features_list = [f.strip() for f in features_input.split(',') if f.strip()]
            feature_objs = [Feature.objects.get_or_create(name=f)[0] for f in features_list]
            project.features.set(feature_objs)

            # Challenges
            challenges_list = [c.strip() for c in challenges_input.split(',') if c.strip()]
            challenge_objs = [Challenge.objects.get_or_create(name=c)[0] for c in challenges_list]
            project.challenges.set(challenge_objs)

            # Outcomes
            outcomes_list = [o.strip() for o in outcomes_input.split(',') if o.strip()]
            outcomes_obj = [Outcome.objects.get_or_create(outcome=o)[0] for o in outcomes_list]
            project.outcomes.set(outcomes_obj)

            # Images
            for img in projimage_input:
                projimage.objects.create(project=project, img=img)

            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   


class ProjectRetrieveView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    

class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
   

class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
