from django.db import models

# Create your models here.

class SavedEmail(models.Model):
    email = models.EmailField(unique=True)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}'

class Home(models.Model):
    # Navigation Links and Dropdown
#     navlink1_name = models.CharField(max_length=200, blank=True, null=True)
#     navlink1_link = models.URLField(blank=True, null=True)
#     navlink2_name = models.CharField(max_length=200, blank=True, null=True)
#     navlink2_link = models.URLField(blank=True, null=True)
#     navlink3_name = models.CharField(max_length=200, blank=True, null=True)
#     navlink3_link = models.URLField(blank=True, null=True)
#     navlink4_name = models.CharField(max_length=200, blank=True, null=True)
#     navlink4_link = models.URLField(blank=True, null=True)
#     navlink5_name = models.CharField(max_length=200, blank=True, null=True)
#     navlink5_link = models.URLField(blank=True, null=True)

#     navlink6_dropdown_name = models.CharField(max_length=200, blank=True, null=True)
#     navlink6_dropdown_item1 = models.CharField(max_length=200, blank=True, null=True)
#     navlink6_dropdown_item1_link = models.URLField(blank=True, null=True)
#     navlink6_dropdown_item2 = models.CharField(max_length=200, blank=True, null=True)
#     navlink6_dropdown_item2_link = models.URLField(blank=True, null=True)


    # Slider section (3 sections)
    slider1_heading = models.CharField(max_length=50, blank=True, null=True)
    slider1_heading_colored = models.CharField(max_length=50, blank=True, null=True)
    slider1_text = models.TextField(blank=True, null=True)
    slider1_button_text = models.CharField(max_length=50, blank=True, null=True)
    slider1_button_url = models.URLField(blank=True, null=True)
    slider1_image = models.ImageField(upload_to='images/home/', blank=True, null=True)
    
#     slider2_heading = models.CharField(max_length=50, blank=True, null=True)
#     slider2_heading_colored = models.CharField(max_length=50, blank=True, null=True)
#     slider2_text = models.TextField(blank=True, null=True)
#     slider2_button_text = models.CharField(max_length=50, blank=True, null=True)
#     slider2_button_url = models.URLField(blank=True, null=True)
#     slider2_image = models.ImageField(upload_to='images/home/', blank=True, null=True)
    
#     slider3_heading = models.CharField(max_length=50, blank=True, null=True)
#     slider3_heading_colored = models.CharField(max_length=50, blank=True, null=True)
#     slider3_text = models.TextField(blank=True, null=True)
#     slider3_button_text = models.CharField(max_length=50, blank=True, null=True)
#     slider3_button_url = models.URLField(blank=True, null=True)
#     slider3_image = models.ImageField(upload_to='images/home/', blank=True, null=True)

    # Who We Are Section (heading, small image and text that shows after hovring over image)
    who_we_heading = models.CharField(max_length=100, blank=True, null=True)
    
    who_we_text = models.TextField(blank=True, null=True)
    

    
    
    image1_text = models.CharField(max_length=100, blank=True, null=True)
    image4_text = models.CharField(max_length=100, blank=True, null=True)
    image6_text = models.CharField(max_length=100, blank=True, null=True)
    
    who_we_1_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_2_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_3_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_4_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_5_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_6_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    

    # Small Slider Section
    small_slider_1_text = models.TextField(blank=True, null=True)
    small_slider_1_designation = models.CharField(max_length=100, blank=True, null=True)
    small_slider_1_person = models.CharField(max_length=100, blank=True, null=True)
    small_slider_1_person_img = models.ImageField(upload_to='images/home/', blank=True, null=True)

    small_slider_2_text = models.TextField(blank=True, null=True)
    small_slider_2_designation = models.CharField(max_length=100, blank=True, null=True)
    small_slider_2_person = models.CharField(max_length=100, blank=True, null=True)
    small_slider_2_person_img = models.ImageField(upload_to='images/home/', blank=True, null=True)

    # Info Slider (5 sections)
    info_slider_1_heading = models.CharField(max_length=100, blank=True, null=True)
    info_slider_1_text = models.TextField(blank=True, null=True)
    info_slider_1_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    info_slider_1_link_name = models.CharField(max_length=100, blank=True, null=True)
    info_slider_1_link = models.URLField(blank=True, null=True)

    info_slider_2_heading = models.CharField(max_length=100, blank=True, null=True)
    info_slider_2_text = models.TextField(blank=True, null=True)
    info_slider_2_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    info_slider_2_link_name = models.CharField(max_length=100, blank=True, null=True)
    info_slider_2_link = models.URLField(blank=True, null=True)

    info_slider_3_heading = models.CharField(max_length=100, blank=True, null=True)
    info_slider_3_text = models.TextField(blank=True, null=True)
    info_slider_3_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    info_slider_3_link_name = models.CharField(max_length=100, blank=True, null=True)
    info_slider_3_link = models.URLField(blank=True, null=True)

    info_slider_4_heading = models.CharField(max_length=100, blank=True, null=True)
    info_slider_4_text = models.TextField(blank=True, null=True)
    info_slider_4_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    info_slider_4_link_name = models.CharField(max_length=100, blank=True, null=True)
    info_slider_4_link = models.URLField(blank=True, null=True)

    info_slider_5_heading = models.CharField(max_length=100, blank=True, null=True)
    info_slider_5_text = models.TextField(blank=True, null=True)
    info_slider_5_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    info_slider_5_link_name = models.CharField(max_length=100, blank=True, null=True)
    info_slider_5_link = models.URLField(blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Home Page'
    
    def __str__(self):
        return 'Home Page'


class Publisher(models.Model):
    # Navigation Links and Dropdown
    publisher_text = models.CharField(max_length=200, blank=True, null=True)
    publisher_button_text = models.CharField(max_length=200, blank=True, null=True)
    publisher_button_url=models.URLField(blank=True, null=True)

    topinfoHeading_r_main = models.CharField(max_length=200, blank=True, null=True)
    sectopinfoHeading_r_sub = models.CharField(max_length=200, blank=True, null=True)


    topinfoHeading_r_topic = models.CharField(max_length=200, blank=True, null=True)
    topinfoHeading_r1 = models.CharField(max_length=200, blank=True, null=True)
    r1_image = models.ImageField(upload_to='images/', blank=True, null=True)
    topinfoHeading_r2 = models.CharField(max_length=200, blank=True, null=True)
    r2_image = models.ImageField(upload_to='images/', blank=True, null=True)
    topinfoHeading_r3 =  models.CharField(max_length=200, blank=True, null=True)
    r3_image = models.ImageField(upload_to='images/', blank=True, null=True)
    topinfoHeading_r4 = models.CharField(max_length=200, blank=True, null=True)
    r4_image = models.ImageField(upload_to='images/', blank=True, null=True)

    topinfoHeading_l_main = models.CharField(max_length=200, blank=True, null=True)
    topinfoHeading_l_sub=models.CharField(max_length=200, blank=True, null=True)

    topinfoHeading_l_topic = models.CharField(max_length=200, blank=True, null=True)
    topinfoHeading_l1 = models.CharField(max_length=200, blank=True, null=True)
    l1_image=models.ImageField(upload_to='images/', blank=True, null=True)
    topinfoHeading_l2 = models.CharField(max_length=200, blank=True, null=True)
    l2_image = models.ImageField(upload_to='images/', blank=True, null=True)

    topinfoHeading_l3 =  models.CharField(max_length=200, blank=True, null=True)
    l3_image = models.ImageField(upload_to='images/', blank=True, null=True)

    topinfoHeading_l4 = models.CharField(max_length=200, blank=True, null=True)
    l4_image = models.ImageField(upload_to='images/', blank=True, null=True)

    businessModel2_main = models.CharField(max_length=200, blank=True, null=True)

    businessModel2_point1 = models.CharField(max_length=500, blank=True, null=True)
    point1_image = models.ImageField(upload_to='images/', blank=True, null=True)

    businessModel2_point2 = models.CharField(max_length=500, blank=True, null=True)
    point2_image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    point2_image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    point2_image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    point2_image4 = models.ImageField(upload_to='images/', blank=True, null=True)
    point2_image5 = models.ImageField(upload_to='images/', blank=True, null=True)
    point2_image6 = models.ImageField(upload_to='images/', blank=True, null=True)

    topSpace_heading = models.CharField(max_length=500, blank=True, null=True)
    topSpace_text = models.CharField(max_length=500, blank=True, null=True)



    def __str__(self):
        return 'Publishers Page'
    
class Advertiser(models.Model):
    advertiser_text = models.CharField(max_length=200, blank=True, null=True)
    advertiser_button_text = models.CharField(max_length=200, blank=True, null=True)
    advertiser_button_url=models.URLField(blank=True, null=True)

    topinfoPara = models.CharField(max_length=200, blank=True, null=True)

    secondParagraph_heading = models.CharField(max_length=200, blank=True, null=True)
    secondParagraph = models.CharField(max_length=200, blank=True, null=True)
    
    topspace1_heading=models.CharField(max_length=200, blank=True, null=True)
    topspace1_text=models.CharField(max_length=200, blank=True, null=True)
    topspace1_image= models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    topspace2_heading = models.CharField(max_length=200, blank=True, null=True)
    topspace2_text = models.CharField(max_length=200, blank=True, null=True)
    topspace2_image = models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    topspace3_heading = models.CharField(max_length=200, blank=True, null=True)
    topspace3_text = models.CharField(max_length=200, blank=True, null=True)
    topspace3_image = models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    topspace4_heading = models.CharField(max_length=200, blank=True, null=True)
    topspace4_text = models.CharField(max_length=200, blank=True, null=True)
    topspace4_image = models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    
    who_we_are=models.CharField(max_length=200, blank=True, null=True)
    who_we_are_description=models.CharField(max_length=500, blank=True, null=True)

    tab_text1 = models.CharField(max_length=200, blank=True, null=True)
    tab_image1 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    tab_content1 = models.CharField(max_length=200, blank=True, null=True)

    tab_text2 = models.CharField(max_length=200, blank=True, null=True)
    tab_image2 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    tab_content2 = models.CharField(max_length=200, blank=True, null=True)

    tab_text3= models.CharField(max_length=200, blank=True, null=True)
    tab_image3 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    tab_content3 = models.CharField(max_length=200, blank=True, null=True)

    tab_text4 = models.CharField(max_length=200, blank=True, null=True)
    tab_image4 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    tab_content4 = models.CharField(max_length=200, blank=True, null=True)

    tab_text5 = models.CharField(max_length=200, blank=True, null=True)
    tab_image5 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    tab_content5 = models.CharField(max_length=200, blank=True, null=True)

    tab_text6 = models.CharField(max_length=200, blank=True, null=True)
    tab_image6 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    tab_content6 = models.CharField(max_length=200, blank=True, null=True)

    
    consectetur=models.CharField(max_length=200, blank=True, null=True)
    consectetur_paragraph = models.CharField(max_length=500, blank=True, null=True)

    row_image1=models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    row_heading1=models.CharField(max_length=200, blank=True, null=True)
    row_paragraph1=models.CharField(max_length=200, blank=True, null=True)

    row_image2 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    row_heading2 = models.CharField(max_length=200, blank=True, null=True)
    row_paragraph2 = models.CharField(max_length=200, blank=True, null=True)

    row_image3 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    row_heading3 = models.CharField(max_length=200, blank=True, null=True)
    row_paragraph3 = models.CharField(max_length=200, blank=True, null=True)


    client_story_heading=models.CharField(max_length=200, blank=True, null=True)

    client_name1=models.CharField(max_length=200, blank=True, null=True)
    client_image1=models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    client_description1=models.CharField(max_length=200, blank=True, null=True)
    client_story1=models.CharField(max_length=2000, blank=True, null=True)

    client_name2 = models.CharField(max_length=200, blank=True, null=True)
    client_image2 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    client_description2 = models.CharField(max_length=200, blank=True, null=True)
    client_story2 = models.CharField(max_length=2000, blank=True, null=True)

    client_name3 = models.CharField(max_length=200, blank=True, null=True)
    client_image3 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)
    client_description3 = models.CharField(max_length=200, blank=True, null=True)
    client_story3 = models.CharField(max_length=2000, blank=True, null=True)

    register_now_heading=models.CharField(max_length=500, blank=True, null=True)
    register_now_description = models.CharField(max_length=500, blank=True, null=True)









    def __str__(self):
        return 'Advertiser Page'
    
    
class Company(models.Model):

    company_text = models.TextField(blank=True, null=True)
    company_button_text = models.CharField(max_length=200, blank=True, null=True)
    company_button_url = models.CharField(max_length=200, blank=True, null=True)

    firstinfo_paragraph = models.TextField(blank=True, null=True)
    secinfo_Heading = models.CharField(max_length=200, blank=True, null=True)
    secinfo_sub = models.CharField(max_length=200, blank=True, null=True)
    secinfo_paragraph = models.TextField(blank=True, null=True)
    secinfo_image1 = models.ImageField(upload_to='images/company', blank=True, null=True)
    secinfo_image2 = models.ImageField(upload_to='images/company', blank=True, null=True)
    secinfo_image3 = models.ImageField(upload_to='images/company', blank=True, null=True)
    secinfo_image4 = models.ImageField(upload_to='images/company', blank=True, null=True)




    progress_heading = models.CharField(max_length=200, blank=True, null=True)

    progress1_name = models.CharField(max_length=200, blank=True, null=True)
    progress1_percentage = models.IntegerField(default=0, blank=True, null=True)

    progress2_name = models.CharField(max_length=200, blank=True, null=True)
    progress2_percentage = models.IntegerField(default=0, blank=True, null=True)

    progress3_name = models.CharField(max_length=200, blank=True, null=True)
    progress3_percentage = models.IntegerField(default=0, blank=True, null=True)



    thirdinfo_heading=models.CharField(max_length=200, blank=True, null=True)
    thirdinfo_paragraph=models.TextField(blank=True, null=True)



    fourthinfo_heading = models.CharField(max_length=200, blank=True, null=True)
    fourthinfo_paragraph = models.TextField(blank=True, null=True)
    fourthinfo_image = models.ImageField(upload_to='images/company', blank=True, null=True)

    icon1=models.ImageField(upload_to='images/company', blank=True, null=True)
    icon2 = models.ImageField(upload_to='images/company', blank=True, null=True)
    icon3 = models.ImageField(upload_to='images/company', blank=True, null=True)



    contact_image = models.ImageField(upload_to='images/', blank=True, null=True)

    company_contact_heading = models.CharField(max_length=200, blank=True, null=True)
    company_contact_para= models.TextField(blank=True, null=True)

    phone_heading= models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    email_heading = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    location_heading = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    getTouch_button_text=models.CharField(max_length=200, blank=True, null=True)
    getTouch_button_url=models.URLField(blank=True, null=True)

    register_button_text = models.CharField(max_length=200, blank=True, null=True)
    register_button_url=models.URLField(blank=True, null=True)

    register_heading = models.CharField(max_length=200, blank=True, null=True)
    register_pargraph = models.TextField(blank=True, null=True)




    def __str__(self):
        return 'Company Page'

    
    
class TrafficPage(models.Model):
    traffic_text = models.CharField(max_length=200, blank=True, null=True)
    traffic_paragraph= models.TextField(blank=True, null=True)
    traffic_button_text = models.CharField(max_length=200, blank=True, null=True)
    traffic_button_url = models.CharField(max_length=200, blank=True, null=True)

    firstinfo_paragraph = models.TextField(blank=True, null=True)

    secinfo_Heading = models.CharField(max_length=200, blank=True, null=True)
    secinfo_point1 = models.CharField(max_length=200, blank=True, null=True)
    secinfo_point2 = models.CharField(max_length=200, blank=True, null=True)

    thirdinfo_image = models.ImageField(upload_to='images/traffic', blank=True, null=True)


    progress_main = models.CharField(max_length=200, blank=True, null=True)

    progress1_heading = models.CharField(max_length=200, blank=True, null=True)
    progress1_text=models.TextField( blank=True, null=True)
    progress1_percentage = models.IntegerField(default=0, blank=True, null=True)

    progress2_heading = models.CharField(max_length=200, blank=True, null=True)
    progress2_text = models.TextField(blank=True, null=True)
    progress2_percentage = models.IntegerField(default=0, blank=True, null=True)

    progress_footer=models.CharField(max_length=200, blank=True, null=True)

    tab_heading = models.CharField(max_length=200, blank=True, null=True)

    tab1 = models.CharField(max_length=200, blank=True, null=True)
    tab1_image = models.ImageField(upload_to='images/traffic', blank=True, null=True)
    tab2 = models.CharField(max_length=200, blank=True, null=True)
    tab2_image = models.ImageField(upload_to='images/traffic', blank=True, null=True)
    tab3 = models.CharField(max_length=200, blank=True, null=True)
    tab3_image = models.ImageField(upload_to='images/traffic', blank=True, null=True)
    tab4 = models.CharField(max_length=200, blank=True, null=True)
    tab4_image = models.ImageField(upload_to='images/traffic', blank=True, null=True)


    register_button_text = models.CharField(max_length=50, blank=True, null=True)
    register_button_url = models.URLField(blank=True, null=True)

    register_heading =models.TextField(blank=True, null=True)
    register_pargraph = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Traffic Page'


    
    
class ContactPage(models.Model):
    contact_text = models.CharField(max_length=200, blank=True, null=True)
    contact_paragraph= models.TextField(blank=True, null=True)
    contact_button_text = models.CharField(max_length=200, blank=True, null=True)
    contact_button_url = models.CharField(max_length=200, blank=True, null=True)

    
    email_heading = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    email_us = models.CharField(max_length=200, blank=True, null=True)



    phone_heading = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    

    address_heading = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    map_link_name=models.CharField(max_length=200, blank=True, null=True)
    map_link = models.URLField(blank=True, null=True)

    social_heading=models.CharField(max_length=200, blank=True, null=True)

    facebook_link = models.URLField( blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)

    business_heading= models.CharField(max_length=200, blank=True, null=True)


    register_button_text = models.CharField(max_length=50, blank=True, null=True)
    register_button_url = models.URLField(blank=True, null=True)

    register_heading =models.TextField(blank=True, null=True)
    register_pargraph = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Contact Page'
class LoginPage(models.Model):
    login_text = models.CharField(max_length=200, blank=True, null=True)
    login_paragraph= models.TextField(blank=True, null=True)

    page_image = models.ImageField(upload_to='images/registration', blank=True, null=True)
    page_text = models.TextField(blank=True, null=True)

    signin_button_text = models.CharField(max_length=200, blank=True, null=True)
    

    dont_have_accout = models.CharField(max_length=200, blank=True, null=True)
    signup_link_name = models.CharField(max_length=200, blank=True, null=True)
    
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    linkdin_link = models.URLField(blank=True, null=True)
 




    def __str__(self):
        return 'Login Page'


class SignUpPage(models.Model):
    signup_text = models.CharField(max_length=200, blank=True, null=True)
    signup_paragraph = models.TextField(blank=True, null=True)

    page_image = models.ImageField(upload_to='images/registration', blank=True, null=True)
    page_text = models.TextField(blank=True, null=True)

    signup_button_text = models.CharField(max_length=200, blank=True, null=True)
    



    already_have_accout = models.CharField(max_length=200, blank=True, null=True)
    login_link_name = models.CharField(max_length=200, blank=True, null=True)
    
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    linkdin_link = models.URLField(blank=True, null=True)
 

    def __str__(self):
        return 'SignUp Page'
