from pta.models import Teacher, ParentalUnit, Homework, WishlistItem, \
    Activity, TodoItem, Message

from django.contrib.auth.models import User

class Sample1:
    teachers = (
        (20,'Victor','Victorious','victor@nadir.org','Astrology'),
        (21,'Wanda','Wilkins','wanda@zenith.com','Biology'),
        (22,'Xavier','Xanadu','xavier@acme.com','Mathematics'),
        (23,'Yolanda','Vega','yolanda@nadir.org','Astronomy'),
    )

    parents = (
        (0,'Alice','Apples','alice@acme.com'),
        (1,'Bob','Bernardo','bob@nadir.org'),
        (2,'Carol','Chernardo','carol@zenith.net'),
        (3,'Dave','Dernardo','dave@acme.com'),
        (4,'Eve','Ernardo','eve@nadir.com'),
        (5,'Frank','Fernardo','frank@nadir.com'),
        (6,'Gloria','Gernardo','gloria@zenith.com'),
        (7,'Henry','Hernardo','henry@acme.com'),
        (8,'Inez','Iernardo','inez@nadir.org'),
        (9,'Jake','Jernardo','jake@zenith.com'),
        (10,'Kat','Kernardo','kat@acme.com'),
        (11, 'Louis','Lernardo','louis@nadir.org'),
        (12, 'Mary','Mernardo', 'mary@zenith.com'),
        (13, 'Noel','Nernardo', 'noel@acme.com'),
        (14, 'Olivia','Ornardo', 'olivia@nadir.org'),
        (15, 'Peter','Pernardo', 'peter@zenith.com'),
        (16, 'Robert','Rernardo', 'robert@acme.com'),
        (17, 'Susan','Sernardo', 'susan@nadir.org'),
        (18, 'Tyler','Ternardo', 'tyler@zenith.com'),
        (19, 'Unelda','Uernardo', 'unelda@acme.com'),
    )

    homework = (
        ('Math problems', 'Do all of page 95 odd problems only.'),
        ('Extra Credit', 'Solve an NP-hard problem'),
        ('English', 'Read all the books in the library for the test'),
    )

    # # index, name, description, president (-1 for none), members
    # clubs = (
    #     (0,'French','Pour les amateurs de la langue francaise',2, (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22)),
    #     (1,'German','Diejenigen, die Deutsch sprechen',1, (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23)),
    #     (2,'Rugby','Intercollegiate Rugby competition',0, (0, 3, 6, 9, 12, 15, 18, 21)),
    #     (3,'Field Hockey','Intramural Field Hockey competition',4, (1, 4, 7, 10, 13, 16, 19, 22)),
    #     )
    # # index, name, description, members
    # groups = (
    #     (0,'International','Clubs interested in international culture', (0, 1, 2)),
    #     (1,'Sports','Clubs involved with sports', (2, 3)),
    #     )


def createSample(data):
    '''
        Use a data hash like that above to create a collection
        of objects
    '''
    tl = []
    for per in data.teachers:
        p = User(
                username=per[1].lower(),
                first_name=per[1],
                last_name=per[2],
                email=per[3],
                )
        pwd = per[1].lower()[0]
        p.set_password(pwd)
        p.save()
        teacher = Teacher(
            user=p,
            classinfo=per[4],
        )
        teacher.save()
        tl.append(teacher)
        print(teacher.user.username, pwd, teacher.classinfo)

    pl = []
    for per in data.parents:
         p = User(
             username=per[1].lower(),
             first_name=per[1],
             last_name=per[2],
             email=per[3],
         )
         pwd = per[1].lower()[0]
         p.set_password(pwd)
         p.save()
         parentalunit = ParentalUnit(
             user=p,
             teacher=tl[per[0]%4],
         )
         parentalunit.save()
         pl.append(parentalunit)
         print(parentalunit.user.username, pwd, parentalunit.teacher)

    i = 0
    for hwdata in data.homework:
        hw = Homework(
            title=hwdata[0],
            description=hwdata[1],
            teacher=tl[i]
        )
        hw.save()
        i+=1


    # cl = []
    # for clb in data.clubs:
    #     c = Club(
    #              name=clb[1],
    #              description=clb[2])
    #     c.save()
    #     for i in clb[4]:
    #         c.members.add(pl[i])
    #     c.president = pl[clb[3]]
    #     c.save()
    #     cl.append(c)
    #
    # #gl = []
    # for gr in data.groups:
    #     g = Group(name=gr[1],
    #              description=gr[2])
    #     g.save()
    #     for i in gr[3]:
    #         g.members.add(cl[i])
    #     #gl.append(g)

