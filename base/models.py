from django.db import models

# Create your models here.

class SavedEmail(models.Model):
    email = models.EmailField(unique=True)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}'

class Home(models.Model):
    # Navigation Links and Dropdown
    navlink1_name = models.CharField(max_length=200, blank=True, null=True)
    navlink1_link = models.URLField(blank=True, null=True)
    navlink2_name = models.CharField(max_length=200, blank=True, null=True)
    navlink2_link = models.URLField(blank=True, null=True)
    navlink3_name = models.CharField(max_length=200, blank=True, null=True)
    navlink3_link = models.URLField(blank=True, null=True)
    navlink4_name = models.CharField(max_length=200, blank=True, null=True)
    navlink4_link = models.URLField(blank=True, null=True)
    navlink5_name = models.CharField(max_length=200, blank=True, null=True)
    navlink5_link = models.URLField(blank=True, null=True)

    navlink6_dropdown_name = models.CharField(max_length=200, blank=True, null=True)
    navlink6_dropdown_item1 = models.CharField(max_length=200, blank=True, null=True)
    navlink6_dropdown_item1_link = models.URLField(blank=True, null=True)
    navlink6_dropdown_item2 = models.CharField(max_length=200, blank=True, null=True)
    navlink6_dropdown_item2_link = models.URLField(blank=True, null=True)


    # Slider section (3 sections)
    slider1_heading = models.CharField(max_length=50, blank=True, null=True)
    slider1_heading_colored = models.CharField(max_length=50, blank=True, null=True)
    slider1_text = models.TextField(blank=True, null=True)
    slider1_button_text = models.CharField(max_length=50, blank=True, null=True)
    slider1_button_url = models.URLField(blank=True, null=True)
    slider1_image = models.ImageField(upload_to='images/home/', blank=True, null=True)
    
    slider2_heading = models.CharField(max_length=50, blank=True, null=True)
    slider2_heading_colored = models.CharField(max_length=50, blank=True, null=True)
    slider2_text = models.TextField(blank=True, null=True)
    slider2_button_text = models.CharField(max_length=50, blank=True, null=True)
    slider2_button_url = models.URLField(blank=True, null=True)
    slider2_image = models.ImageField(upload_to='images/home/', blank=True, null=True)
    
    slider3_heading = models.CharField(max_length=50, blank=True, null=True)
    slider3_heading_colored = models.CharField(max_length=50, blank=True, null=True)
    slider3_text = models.TextField(blank=True, null=True)
    slider3_button_text = models.CharField(max_length=50, blank=True, null=True)
    slider3_button_url = models.URLField(blank=True, null=True)
    slider3_image = models.ImageField(upload_to='images/home/', blank=True, null=True)

    # Who We Are Section (heading, small image and text that shows after hovring over image)
    who_we_1_heading = models.CharField(max_length=100, blank=True, null=True)
    who_we_1_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_1_text = models.TextField(blank=True, null=True)

    who_we_2_heading = models.CharField(max_length=100, blank=True, null=True)
    who_we_2_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_2_text = models.TextField(blank=True, null=True)

    who_we_3_heading = models.CharField(max_length=100, blank=True, null=True)
    who_we_3_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_3_text = models.TextField(blank=True, null=True)

    who_we_4_heading = models.CharField(max_length=100, blank=True, null=True)
    who_we_4_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_4_text = models.TextField(blank=True, null=True)

    who_we_5_heading = models.CharField(max_length=100, blank=True, null=True)
    who_we_5_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_5_text = models.TextField(blank=True, null=True)

    who_we_6_heading = models.CharField(max_length=100, blank=True, null=True)
    who_we_6_img = models.ImageField(upload_to='images/home/', blank=True, null=True)
    who_we_6_text = models.TextField(blank=True, null=True)

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

    topinfoPara = models.CharField(max_length=200, blank=True, null=True)

    secondParagraph_heading = models.CharField(max_length=200, blank=True, null=True)
    secondParagraph = models.CharField(max_length=200, blank=True, null=True)


    tab_text1 = models.CharField(max_length=200, blank=True, null=True)
    tab_image1 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    tab_text2 = models.CharField(max_length=200, blank=True, null=True)
    tab_image2 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    tab_text3= models.CharField(max_length=200, blank=True, null=True)
    tab_image3 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    tab_text4 = models.CharField(max_length=200, blank=True, null=True)
    tab_image4 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    tab_text5 = models.CharField(max_length=200, blank=True, null=True)
    tab_image5 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    tab_text6 = models.CharField(max_length=200, blank=True, null=True)
    tab_image6 = models.ImageField(upload_to='images/advertiser', blank=True, null=True)

    thirdParagraph_heading = models.CharField(max_length=200, blank=True, null=True)
    thirdParagraph = models.CharField(max_length=200, blank=True, null=True)






    def __str__(self):
        return 'Advertiser Page'
