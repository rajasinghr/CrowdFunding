#dataframes created to load data from files

import pandas as pd

tableColumnNames = {}

projects = pandas.read_csv('../data/opendata_projects000.gz', escapechar='\\', names=['_projectid', '_teacher_acctid', '_schoolid', 'school_ncesid', 'school_latitude', 'school_longitude', 'school_city', 'school_state', 'school_zip', 'school_metro', 'school_district', 'school_county', 'school_charter', 'school_magnet', 'school_year_round', 'school_nlns', 'school_kipp', 'school_charter_ready_promise', 'teacher_prefix', 'teacher_teach_for_america', 'teacher_ny_teaching_fellow', 'primary_focus_subject', 'primary_focus_area' ,'secondary_focus_subject', 'secondary_focus_area', 'resource_type', 'poverty_level', 'grade_level', 'vendor_shipping_charges', 'sales_tax', 'payment_processing_charges', 'fulfillment_labor_materials', 'total_price_excluding_optional_support', 'total_price_including_optional_support', 'students_reached', 'total_donations', 'num_donors', 'eligible_double_your_impact_match', 'eligible_almost_home_match', 'funding_status', 'date_posted', 'date_completed', 'date_thank_you_packet_mailed', 'date_expiration'])


tableColumnNames['Projects'] = list(projects.columns.values)
projects.shape


projects[pandas.DatetimeIndex(projects['date_posted']).year == 2015].shape



projects.head(1)



donations = pandas.read_csv('../data/opendata_donations000.gz', escapechar='\\', names=['_donationid', '_projectid', '_donor_acctid', '_cartid', 'donor_city', 'donor_state', 'donor_zip', 'is_teacher_acct', 'donation_timestamp', 'donation_to_project', 'donation_optional_support', 'donation_total', 'donation_included_optional_support', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched', 'is_teacher_referred', 'giving_page_id', 'giving_page_type', 'for_honoree', 'thank_you_packet_mailed'])

donations.shape


tableColumnNames['Donations'] = list(donations.columns.values)


resources = pandas.read_csv('../data/opendata_resources000.gz', escapechar='\\', names=['_resourceid', '_projectid', 'vendorid', 'vendor_name', 'item_name', 'item_number', 'item_unit_price', 'item_quantity'])


resources.shape


tableColumnNames['Resources'] = list(resources.columns.values) 


resources.head(5)


essays = pandas.read_csv('../data/opendata_essays000.gz', escapechar='\\', names=['_projectid', '_teacherid', 'title', 'short_description', 'need_statement', 'essay', 'thankyou_note', 'impact_letter'])


essays.head(1)


essays.shape

tableColumnNames['Essays'] = list(essays.columns.values)


giving_pages = pandas.read_csv('../data/opendata_giving_pages000.gz', escapechar='\\', names=['giving_page_id', '_creator_acctid', 'created_date', 'is_active', 'most_recent_donation', 'amount_raised', 'number_of_donors', 'number_of_students', 'number_of_projects_supported', 'number_of_teachers', 'number_of_schools'])

giving_pages.shape



tableColumnNames['Giving Pages'] = list(giving_pages.columns.values)



giving_pages.head(5)



giving_page_projects = pandas.read_csv('../data/opendata_giving_page_projects000.gz', escapechar='\\', names=['giving_page_id', '_projectid'])



giving_page_projects.head(5)


giving_page_projects.shape


tableColumnNames['Giving Page Projects'] = list(giving_page_projects.columns.values)


# In[34]:


giftcards = pandas.read_csv('../data/opendata_giftcards000.gz', escapechar='\\', names=['_giftcardid', 'dollar_tier', '_buyer_acctid', 'buyer_city', 'buyer_state', 'buyer_zip', 'date_purchased', '_buyer_cartid', '_recipient_acctid', 'recipient_city', 'recipient_state', 'recipient_zip', 'redeemed', 'date_redeemed', '_redeemed_cartid', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched'])


# In[35]:


giftcards.head(1)


# In[36]:


giftcards.shape


# In[44]:


tableColumnNames['Giftcards'] = list(giftcards.columns.values)


# In[45]:


tableColumnNames


# In[58]:


import xlsxwriter


# In[59]:


workbook = xlsxwriter.Workbook('Data Columns.xlsx')
worksheet = workbook.add_worksheet()


# In[60]:




for key in tableColumnNames.keys():
    row = 0
    worksheet.write(row, col, key)
    for item in tableColumnNames[key]:
        row += 1
        worksheet.write(row, col, item)
        
    col = col+1

workbook.close()

