from django.core.management.base import BaseCommand
from pta.models import TeamMember

class OurTeam:
    member = (
        ('Chen Chen','Chen Chen is a Senior in Computer Science at Kennesaw State University.  He enjoys many MOBA games like League of Legends, Overwatch, and Heroes of the Storm.','ChenChen.jpg'),
        ('Jeremy Sloan','insert description here','cleanallthethings.png'),
        ('Ross Taylor','Ross Taylor is a Senior at KSU graduating in December with a degree in Computer Science.','RossTaylor.jpg'),
        ('Suat Iskender','Suat Iskender is a Senior in Computer Science at Kennesaw State University.  He joined the Collaborate! team in July.  When he is not coding, he enjoys long walks in the park and playing Heroes of the Storm.','SuatIskender.jpg'),
    )

class Command(BaseCommand):
    help = "add in team member information"

    def handle(self, *args, **options):
        for person in OurTeam.member:
            per = TeamMember(
                fullname=person[0],
                description=person[1],
                imagename=person[2]
            )
            per.save()

