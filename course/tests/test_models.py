from django.test import TestCase
from catalog.models import Course, Branch, Category, Contact

class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        category=Category.objects.create(name='творческий предмет',
         imgpath='ffrfrg')
        branch=Branches.objects.create(latitude=27364553,
        longitude = 4454356,
        adress= 'улица калинина')
        contact=Contacts.objects.create(type=1,value= 999809810)
        course=Course.objects.create(name= 'рисование',
            description='бла бла бла',
            logo='кисть')

    def test_Course(self):
        course_name=Course.objects.get(id=1).course.name
        course_logo=Course.objects.get(id=1).course.logo
        max_length_name = Course._meta.get_field("name").max_length_name
        max_length_desc = Course._meta.get_field("description").max_length_desc
        self.assertEquals(max_length_desc,255)
        self.assertEquals(max_length_name,20)
        self.assertEquals(course_name, 'рисование')
        self.assertEquals(course_logo, 'кисть')

    def test_Category(self):
        course_img=Course.objects.get(id=1).category.imgpath
        category_name=Course.objects.get(id=1).contact.name
        self.assertEquals(category_name,'творческий предмет')
        self.assertEquals(img, 'ffrfrg')

    def test_Contact(self):
        contact_type=Course.objects.get(id=1).category.choices
        contact_value=Course.objects.get(id=1).contact.value
        self.assertEquals(contact_type, 1)
        self.assertEquals(value, 999809810)

    def test_Branch(self):
        branch_latitude=Course.objects.get(id=1).category.latitude
        branch_longitude=Course.objects.get(id=1).category.longitude
        branch_adress=Course.objects.get(id=1).category.adress
        self.assertEquals(branch_latitude, 27364553)
        self.assertEquals(branch_latitude, 4454356)
        self.assertEquals(branch_adress, 'улица калинина')

    