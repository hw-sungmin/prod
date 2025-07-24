#가상환경 추가  virtualenv --python=python3.12.6 venv
#가상환경 실행  source venv/bin/activate
#가상환경 종료  deactivate
#셀레니움 설치  pip install selenium
#webdriver_manager 설치 pip install webdriver_manager
#크롬 드라이버 오토 인스톨러 설치   pip install chromedriver_autoinstaller
#push  // git push -u orign main



########## 검증 시 변경 필수 ##########

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# 드라이버 설정
options = Options()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window() #브라우저 최대화 설정
driver.get("https://crm.assistfit.co.kr/") #crm 메인 페이지 진입

# driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", "popup-hidden-team-flex", "2025-07-24")

# driver.refresh()

# 호출 횟수 추적용 변수
wait_count = 0

# 고유값 생성 (상품명)
def generate_random_korean_name():
    korean_chars = [chr(i) for i in range(0xAC00, 0xD7A4)]  # 유니코드 한글 범위 (가 ~ 힣)
    return ''.join(random.choices(korean_chars, k=6))  # 랜덤 한글 6글자 생성

# 랜덤 휴대전화번호 생성 함수 (휴대전화 번호_회원)
def generate_random_member_number():
    random_suffix = ''.join(random.choices('0123456789', k=5))  # 0-9 숫자 5자리 랜덤 생성
    return f"010000{random_suffix}"  # 고정된 앞자리와 랜덤 5자리 결합

# 랜덤 휴대전화번호 생성 함수 (휴대전화 번호_직원)
def generate_random_employee_number():
    random_suffix = ''.join(random.choices('0123456789', k=5))  # 0-9 숫자 5자리 랜덤 생성
    return f"010100{random_suffix}"  # 고정된 앞자리와 랜덤 5자리 결합

# 아이디, 비밀번호, 로그인 버튼의 셀렉터 설정
id_selector = "#mobileNumber"
password_selector = "#password"
login_button_selector = "body > section > div > div.w-full.bg-\[--netural-gray-scale-white\].rounded-lg.border.border-\[var\(--netural-gray-scale-100\].overflow-y-auto > div > div.w-full.flex.flex-col.gap-\[1\.25rem\] > div > form > div.flex.flex-col.gap-4 > button"

# 아이디, 비밀번호 입력 및 로그인 버튼 클릭
def login(id, password):
    global wait_count  # 글로벌 변수 선언
    try:
        # 아이디 입력 호출 대기 및 값 입력
        wait_count += 3  # WebDriverWait 호출 시 카운터 증가
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, id_selector))
        )
        id_field = driver.find_element(By.CSS_SELECTOR, id_selector)
        id_field.clear()
        id_field.send_keys("01043931593")
        print("아이디 입력 완료")

        # 비밀번호 입력 호출 대기 및 값 입력
        password_field = driver.find_element(By.CSS_SELECTOR, password_selector)
        password_field.clear()
        password_field.send_keys("qwer1234")
        print("비밀번호 입력 완료")

        # 로그인 버튼 클릭
        login_button = driver.find_element(By.CSS_SELECTOR, login_button_selector)
        login_button.click()
        print("로그인 버튼 클릭 완료")

    except Exception as e:
        print(f"!!!!! 로그인 과정에서 오류 발생: {e} !!!!!")


# 프랜차이즈 선택
franchise_selector = "body > section > div > div.w-full.bg-\[--netural-gray-scale-white\].rounded-lg.border.border-\[var\(--netural-gray-scale-100\].overflow-y-auto > div > div > div.flex-1.flex.flex-col.gap-\[1\.25rem\].py-\[1\.875rem\] > a:nth-child(1)"

# 첫 번째 프랜차이즈 선택
def select_first_franchise():
    global wait_count  # 글로벌 변수 선언
    try:
        # 프랜차이즈 목록 호출 대기
        wait_count += 1  # WebDriverWait 호출 시 카운터 증가
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, franchise_selector))
        )
        franchise = driver.find_element(By.CSS_SELECTOR, franchise_selector)
        franchise.click()
        print("첫 번째 프랜차이즈 선택 완료")

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 프랜차이즈 선택 관련 오류 발생 !!!!!")

select_first_franchise()
time.sleep(1)

# 로그인
user_id = "your_user_id"
user_password = "your_password"
login(user_id, user_password)
time.sleep(1)

#이벤트 공지 닫기
event_close_selector = "body > div.fixed.inset-0.z-50.bg-black\/60.flex.items-center.justify-center > div > div > button:nth-child(2)"

def event_close():
    global wait_count
    try:
        wait_count += 1
        WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, event_close_selector))
        )
        event = driver.find_element(By. CSS_SELECTOR, event_close_selector)
        event.click()
        print("이벤트 팝업 닫기 완료")
    
    except TimeoutException:
        print("⏩ 이벤트 팝업 없음 (정상) → 계속 진행")

    except (NoSuchElementException, Exception) as e:
        print(f"⚠️ 이벤트 팝업 처리 중 오류 발생: {e}")

event_close()
time.sleep(1)


#현재 센터 선택 후 특정 지점 선택
center_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > button"
center_xpath = "//button[text()='APT 강북점']"  ########## 검증 시 변경 항목 (테스트 환경에 맞는 지점명) ###########

#현재 센터 선택 및 지점 변경
def select_center():
    global wait_count # 글로벌 변수 선언
    try:
        #현재 센터 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, center_selector))
        )
        center = driver.find_element(By.CSS_SELECTOR, center_selector)
        center.click()
        print("현재 센터 선택 완료")

        # 현재 센터 선택 후 딜레이 2초
        time.sleep(1)

        # 특정 지점 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, center_xpath))
        )
        center_select = driver.find_element(By.XPATH, center_xpath)
        center_select.click()
        print("특정 지점 선택 완료")
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 현재 센터 관련 오류 발생 !!!!!")

select_center()
time.sleep(1)


#센터 정보 선택 및 수정 동작
center_informaiton_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(2) > li"
center_information_notice_kiosk_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.flex.flex-1.flex-col.gap-5.pt-5.px-36.pb-10 > div.h-\[3\.0625rem\].flex.justify-between.items-center > div.flex.gap-2 > button:nth-child(2) > p"
center_information_notice_app_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.flex.flex-1.flex-col.gap-5.pt-5.px-36.pb-10 > div.h-\[3\.0625rem\].flex.justify-between.items-center > div > button:nth-child(1) > p"
center_information_center_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5.px-10 > ul > li:nth-child(2) > button"
center_information_notice_app_create_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > footer > a > button"
center_informaiton_update_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > footer > a > button"
center_informaiton_save_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > button"
center_informaiton_notice_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5.px-10 > ul > li:nth-child(1) > button"




def center_information():
    global wait_count # 글로벌 변수 선언
    try:
        #센터 정보 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, center_informaiton_selector))
        )
        center = driver.find_element(By.CSS_SELECTOR, center_informaiton_selector)
        center.click()
        print("센터 정보 선택 완료")

        #센터 정보 선택 후 딜레이 2초
        time.sleep(1)

        #공지 사항 _ 키오스크 공지 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, center_information_notice_kiosk_selector))
        )
        center_information_notice_kiosk = driver.find_element(By. CSS_SELECTOR, center_information_notice_kiosk_selector)
        center_information_notice_kiosk.click()
        print("키오스크 공지 선택 완료")
        time.sleep(1)

        #공지 사항 _ 회원 앱 공지 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, center_information_notice_app_selector))
        )
        center_information_notice_app = driver.find_element(By. CSS_SELECTOR, center_information_notice_app_selector)
        center_information_notice_app.click()
        print("회원 앱 공지 선택 완료")
        time.sleep(1)

        #공지 사항 _ 회원 앱 _ 게시물 작성 공지 선택
        wait_count += 2
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, center_information_notice_app_create_selector))
        )
        center_information_notice_app_create = driver.find_element(By. CSS_SELECTOR, center_information_notice_app_create_selector)
        center_information_notice_app_create.click()
        print("회원 앱 공지 _ 게시물 작성 선택 완료")
        time.sleep(1)

        #이전 화면 이동
        driver.back()
        print("이전 페이지 이동 완료")
        time.sleep(1)
        
        #센터 정보 탭 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, center_information_center_selector))
        )
        enter_information_center = driver.find_element(By.CSS_SELECTOR, center_information_center_selector)
        enter_information_center.click()
        print("센터 정보 탭 선택 완료")

        #내용 수정 선택 후 딜레이 2초
        time.sleep(1)

        #센터 정보 내용 수정 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, center_informaiton_update_selector))
        )
        center_select = driver.find_element(By.CSS_SELECTOR, center_informaiton_update_selector)
        center_select.click()
        print("내용 수정 선택 완료")

        #내용 수정 선택 후 딜레이 2초
        time.sleep(1)

        #저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, center_informaiton_save_selector))
        )
        center_select = driver.find_element(By.CSS_SELECTOR, center_informaiton_save_selector)
        center_select.click()
        print("저장 선택 완료")

        #저장 선택 후 딜레이 2초
        time.sleep(1)

        #센터 정보 _ 공지 사항 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, center_informaiton_notice_selector))
        )
        center_informaiton_notice = driver.find_element(By. CSS_SELECTOR, center_informaiton_notice_selector)
        center_informaiton_notice.click()
        print("공지 사항 선택 완료")
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 센터 정보 관련 오류 발생 !!!!!")

center_information()
time.sleep(1)


#회원 관리_회원 등록 동작
member_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(3) > li"
member_information_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(1) > button"
member_info_check_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.flex-1.flex.flex-col.gap-4.px-10.pb-10 > table > tbody > tr:nth-child(1)"
member_revise_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.flex.flex-col.px-10 > div > div.flex.col-span-2.gap-5.pt-6 > div.flex.flex-col.gap-4 > a > button"
member_revise_save_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > div > button"
member_create_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > a > button"
member_create_select_selector = "body > div.flex.justify-center.items-center.fixed.inset-0.z-50.backdrop-filter.placeholder\:outline-none.focus\:outline-none.cursor-auto.duration-300.h-\[100svh\].rounded-md.bg-black\/60.backdrop-blur-sm > div > div > div > div.flex-auto.items-center > div > div:nth-child(1) > a"
member_datail_name_selector = "#username"
member_datail_mobile_selector = "#mobileNumber"
member_dropdown_selector = 'button.inline-flex.justify-between.w-full.bg-transparent'
member_dropdown_option_xpath = "//button[text()='워크인']"
item_add_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > div > a > button"
item_add_save_selector = "body > div.flex.justify-center.items-center.fixed.inset-0.z-50.backdrop-filter.placeholder\:outline-none.focus\:outline-none.cursor-auto.duration-300.h-\[100svh\].bg-black\/60.backdrop-blur-sm > div > div > div > div > main > div > button"
item_tab_GX_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > ul > li:nth-child(2) > button > p"
item_tab_PT_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > ul > li:nth-child(3) > button > p"
item_tab_locker_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > ul > li:nth-child(4) > button > p"
item_tab_equipment_selector = "#member-detail-create > div.flex.flex-col.gap-4 > div > ul > li:nth-child(5) > button > p"
member_save_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > div > button"
member_secession_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(2) > button"
member_refund_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(3) > button"
member_refund_history_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(2) > button"
member_group_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(4) > button"
member_history_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(5) > button"
pause_history_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.w-full.px-10.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(6) > button"
item_add_confirm_selector = "#member-payment > div.flex.justify-center.items-center.fixed.inset-0.z-50.bg-black\/10.backdrop-filter.placeholder\:outline-none.focus\:outline-none.cursor-auto.duration-300 > div > div > div > div > div.h-\[3\.125rem\].flex.items-center.self-stretch > button:nth-child(3)"


def member_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #회원 관리 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_selector))
        )
        member = driver.find_element(By.CSS_SELECTOR, member_selector)
        member.click()
        print("회원 관리 선택 완료")

        #회원 관리 선택 후 딜레이 2초
        time.sleep(1)
        
        #회원 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_create_selector))
        )
        member_create = driver.find_element(By.CSS_SELECTOR, member_create_selector)
        member_create.click()
        print("회원 관리_회원 등록 선택 완료")

        #회원 등록 선택 후 딜레이 2초
        time.sleep(1)

        #상세 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_create_select_selector))
        )
        member_datail = driver.find_element(By.CSS_SELECTOR, member_create_select_selector)
        member_datail.click()
        print("회원 관리_회원 등록_상세 등록 선택 완료")
        
        #상세 등록 선택 후 딜레이 2초
        time.sleep(1)

        # 이름 입력 호출 대기 및 값 입력
        wait_count += 2
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, member_datail_name_selector))
        )
        name_field = driver.find_element(By.CSS_SELECTOR, member_datail_name_selector)
        name_field.clear()
        name_field.send_keys("자동화검증회원") 
        print("이름 입력 완료")

        # 비밀번호 입력 호출 대기 및 값 입력
        mobile_No_field = driver.find_element(By.CSS_SELECTOR, member_datail_mobile_selector)
        mobile_No_field.clear()
        random_phone = generate_random_member_number()
        mobile_No_field.send_keys(random_phone)
        print("휴대전화번호 입력 완료")

        # 아이디, 비밀번호 입력 후 2초 딜레이
        time.sleep(1)

        #방문 경로 드롭다운 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_dropdown_selector))
        )
        member_dropdown = driver.find_element(By.CSS_SELECTOR, member_dropdown_selector)
        member_dropdown.click()
        print("방문 경로 드롭다운 선택 완료")

        #회원 관리 선택 후 딜레이 2초
        time.sleep(1)

        #방문 경로 드롭다운_특정값 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, member_dropdown_option_xpath))
        )
        member_dropdown_option = driver.find_element(By.XPATH, member_dropdown_option_xpath)
        member_dropdown_option.click()
        print("드롭다운 워크인 선택 완료")

        #방문 경로 선택 후 딜레이 2초
        time.sleep(1)

        #회원권 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #회원권 상품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #회원권 상품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")
        time.sleep(1)

  
#그룹 수업 탭 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_tab_GX_selector))
        )
        item_tab_GX = driver.find_element(By.CSS_SELECTOR, item_tab_GX_selector)
        item_tab_GX.click()
        print("그룹 수업 탭 선택 완료")

        # 그룹 수업 탭 선택 후 딜레이 2초
        time.sleep(1)

        #그룹 수업 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #그룹 수업 상품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #그룹 수업 상품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")


        #개인 레슨 탭 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_tab_PT_selector))
        )
        item_tab_PT = driver.find_element(By.CSS_SELECTOR, item_tab_PT_selector)
        item_tab_PT.click()
        print("개인 레슨 탭 선택 완료")

        # 개인레슨 탭 선택 후 딜레이 2초
        time.sleep(1)

        #개인 레슨 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #개인 레슨 상품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #개인 레슨 상품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")

        #락커 상품 탭 선택 호출 대기
        wait_count += 1 
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_tab_locker_selector))
        )
        item_tab_locker = driver.find_element(By.CSS_SELECTOR, item_tab_locker_selector)
        item_tab_locker.click()
        print("락커 상품 탭 선택 완료")

        #락커 상품 탭 선택 후 딜레이 2초
        time.sleep(1)

        #락커 상품 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #락커 상품 상품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #락커 상품 상품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")
        time.sleep(1)

        #운동 용품 탭 선택 호출 대기 
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_tab_equipment_selector))
        )
        item_tab_equipment = driver.find_element(By.CSS_SELECTOR, item_tab_equipment_selector)
        item_tab_equipment.click()
        print("운동 용품 탭 선택 완료")

        #운동 용품 탭 선택 후 딜레이 2초
        time.sleep(1)

        #운동 용품 상품 등록 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_selector))
        )
        item_add = driver.find_element(By.CSS_SELECTOR, item_add_selector)
        item_add.click()
        print("상품 등록 선택 완료")

        #운동 용품 등록 선택 후 딜레이 2초
        time.sleep(1)

        #운동 용품 등록 저장 선택 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_save_selector))
        )
        item_add_save = driver.find_element(By.CSS_SELECTOR, item_add_save_selector)
        item_add_save.click()
        print("상품 저장 선택 완료")

        #상품 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #상품 등록 완료 확인 팝업 _ 닫기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, item_add_confirm_selector))
        )
        item_add_confirm = driver.find_element(By.CSS_SELECTOR, item_add_confirm_selector)
        item_add_confirm.click()
        print("닫기 선택 완료")
        time.sleep(1)

        #회원 등록 버튼 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_save_selector))
        )
        member_save = driver.find_element(By.CSS_SELECTOR, member_save_selector)
        member_save.click()
        print("회원 등록 완료")

        #회원 등록 선택 후 선택 후 딜레이 2초
        time.sleep(1)

        #탈퇴 처리 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_secession_selector))
        )
        member_secession = driver.find_element(By.CSS_SELECTOR, member_secession_selector)
        member_secession.click()
        print("회원 삭제 탭 선택 완료")

        #탈퇴 처리 탭 선택 후 딜레이 2초
        time.sleep(1)

        #환불 처리 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_refund_selector))
        )
        member_refund = driver.find_element(By.CSS_SELECTOR, member_refund_selector)
        member_refund.click()
        print("환불 처리 탭 선택 완료")

        #환불 처리 탭 선택 후 딜레이 2초
        time.sleep(1)

        #환불 처리_환불 내역 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_refund_history_selector))
        )
        member_refund_history = driver.find_element(By.CSS_SELECTOR, member_refund_history_selector)
        member_refund_history.click()
        print("환불 처리_환불 내역 탭 선택 완료")

        #환불 처리_환불 내역 탭 선택 후 딜레이 2초
        time.sleep(1)

        #단체 연장 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_group_selector))
        )
        member_group = driver.find_element(By.CSS_SELECTOR, member_group_selector)
        member_group.click()
        print("단체 연장 탭 선택 완료")

        #단체 연장 탭 선택 후 딜레이 2초
        time.sleep(1)

        #정지 기록 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, member_history_selector))
        )
        member_history = driver.find_element(By.CSS_SELECTOR, member_history_selector)
        member_history.click()
        print("정지 기록 탭 선택 완료")

        #정지 기록 탭 선택 후 딜레이 2초
        time.sleep(1)

        #수정 기록 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, pause_history_selector))
        )
        pause_history = driver.find_element(By.CSS_SELECTOR, pause_history_selector)
        pause_history.click()
        print("수정 기록 탭 선택 완료")

        #정지 기록 탭 선택 후 딜레이 2초
        time.sleep(1)

        #회원 정보 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, member_information_selector))
        )
        member_information = driver.find_element(By. CSS_SELECTOR, member_information_selector)
        member_information.click()
        print("회원 정보 탭 선택 완료")

        #회원 정보 탭 선택 후 딜레이 2초
        time.sleep(1)

        #회원 정보_정보 조회 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, member_info_check_selector))
        )
        member_info_check = driver.find_element(By. CSS_SELECTOR, member_info_check_selector)
        member_info_check.click()
        print("회원 정보_정보 조회 선택 완료")

        #회원 정보_정보 조회 선택 후 딜레이 2초
        time.sleep(1)

        #회원 정보 수정 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, member_revise_selector))
        )
        member_revise = driver.find_element(By. CSS_SELECTOR, member_revise_selector)
        member_revise.click()
        print("회원 수정 선택 완료")

        #회원 정보 수정 선택 후 딜레이 2초
        time.sleep(1)

        #회원 정보 수정 저장 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, member_revise_save_selector))
        )
        member_revise_save = driver.find_element(By. CSS_SELECTOR, member_revise_save_selector)
        member_revise_save.click()
        print("회원 정보 수정 저장 완료")

        #회원 정보 수정 저장 후 딜레이 2초
        time.sleep(1)


    except (NoSuchElementException, TimeoutException):
        print("!!!!! 회원 관리 관련 오류 발생 !!!!!")

member_admin()
time.sleep(1)


#직원 관리 동작
employee_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(4) > li"
employee_add_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > a > button"
employee_create_name_selector = "#name"
employee_create_mobile_selector = "#mobileNumber"
employee_member_selector = "#employee-create > div.p-5.flex.flex-col.gap-4.white-box.bg-\[--netural-gray-scale-white\] > div.grid.grid-cols-3.gap-4 > div:nth-child(1) > div.absolute.right-4.flex.items-center.gap-2"
employee_GX_selector = "#employee-create > div.p-5.flex.flex-col.gap-4.white-box.bg-\[--netural-gray-scale-white\] > div.grid.grid-cols-3.gap-4 > div:nth-child(2) > div.absolute.right-4.flex.items-center.gap-2"
employee_PT_selector = "#employee-create > div.p-5.flex.flex-col.gap-4.white-box.bg-\[--netural-gray-scale-white\] > div.grid.grid-cols-3.gap-4 > div:nth-child(3) > div.absolute.right-4.flex.items-center.gap-2"
employee_add_save_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > div > button"
employee_info_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.flex-col.gap-4.pt-5 > div > table > tbody > tr:nth-child(1)"
employee_info_revise_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.px-10.pt-\[1\.875rem\].flex.flex-col.bg-\[--netural-gray-scale-white\] > div > div.flex.col-span-2.gap-5.pt-6 > div.flex.flex-col.gap-4 > a > button"
employee_info_revise_save_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > div > button"
employee_default_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-\[0\.625rem\] > ul > li:nth-child(1) > button"
employee_fire_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-\[0\.625rem\] > ul > li:nth-child(2) > button"
employee_fire_info_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-\[0\.625rem\] > button"
employee_join_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-\[0\.625rem\] > ul > li:nth-child(3) > button"

def employee_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #직원 관리 선택 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_selector))
        )
        employee = driver.find_element(By. CSS_SELECTOR, employee_selector)
        employee.click()
        print("직원 관리 선택 완료")

        #직원 관리 선택 후 딜레이 2초
        time.sleep(1)

        #직원 관리_퇴사 처리 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_fire_selector))
        )
        employee_fire = driver.find_element(By. CSS_SELECTOR, employee_fire_selector)
        employee_fire.click()
        print("직원 관리_퇴사 처리 선택 완료")

        #퇴사 처리 선택 후 딜레이 2초
        time.sleep(1)

        #퇴사 처리_퇴사자 조회 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_fire_info_selector))
        )
        employee_fire_info = driver.find_element(By. CSS_SELECTOR, employee_fire_info_selector)
        employee_fire_info.click()
        print("퇴사자 조회 선택 완료")

        #퇴사자 조회 선택 후 딜레이 2초
        time.sleep(1)

        #직원 관리_가입 관리 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_join_selector))
        )
        employee_join = driver.find_element(By. CSS_SELECTOR, employee_join_selector)
        employee_join.click()
        print("직원 관리_가입 관리 선택 완료")

        #가입 관리 선택 후 딜레이 2초
        time.sleep(1)

        #직원 정보 탭 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_default_selector))
        )
        employee_default = driver.find_element(By. CSS_SELECTOR, employee_default_selector)
        employee_default.click()
        print("직원 정보 선택 완료")

        #직원 정보 선택 후 딜레이 2초
        time.sleep(1)

        #직원 관리_직원 등록 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_add_selector))
        )
        employee_add = driver.find_element(By. CSS_SELECTOR, employee_add_selector)
        employee_add.click()
        print("직원 관리_직원 등록 선택 완료")

        #직원 등록 선택 후 딜레이 2초
        time.sleep(1)

        # 이름 입력 호출 대기 및 값 입력
        wait_count += 2
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, employee_create_name_selector))
        )
        name_field = driver.find_element(By.CSS_SELECTOR, employee_create_name_selector)
        name_field.clear()
        name_field.send_keys("자동화직원")
        print("이름 입력 완료")

        # 비밀번호 입력 호출 대기 및 값 입력
        mobile_No_field = driver.find_element(By.CSS_SELECTOR, employee_create_mobile_selector)
        mobile_No_field.clear()
        random_phone = generate_random_employee_number()
        mobile_No_field.send_keys(random_phone)
        print("휴대전화번호 입력 완료")

        # 아이디, 비밀번호 입력 후 2초 딜레이
        time.sleep(1)

        #수업 권한 설정
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_member_selector))
        )
        employee_member = driver.find_element(By. CSS_SELECTOR, employee_member_selector)
        employee_member.click()
        print("회원권 권한 전체 선택 완료")
        time.sleep(1)

        #수업 권한 설정
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_GX_selector))
        )
        employee_GX = driver.find_element(By. CSS_SELECTOR, employee_GX_selector)
        employee_GX.click()
        print("그룹 수업 권한 전체 선택 완료")
        time.sleep(1)

        #수업 권한 설정
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_PT_selector))
        )
        employee_PT = driver.find_element(By. CSS_SELECTOR, employee_PT_selector)
        employee_PT.click()
        print("개인 레슨 권한 전체 선택 완료")
        time.sleep(1)


        #직원 등록_저장 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_add_save_selector))
        )
        employee_add = driver.find_element(By. CSS_SELECTOR, employee_add_save_selector)
        employee_add.click()
        print("직원 등록_저장 선택 완료")

        #직원 등록 선택 후 딜레이 2초
        time.sleep(1)

        #직원 정보_정보 조회 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_info_selector))
        )
        employee_info = driver.find_element(By. CSS_SELECTOR, employee_info_selector)
        employee_info.click()
        print("직원 정보 조회 선택 완료")

        #직원 정보 조회 선택 후 딜레이 2초
        time.sleep(1)

        #직원 수정 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_info_revise_selector))
        )
        employee_info_revise = driver.find_element(By. CSS_SELECTOR, employee_info_revise_selector)
        employee_info_revise.click()
        print("직원 수정 선택 완료")

        #직원 수정 선택 후 딜레이 2초
        time.sleep(1)

        #직원 수정_저장 호출 대기
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, employee_info_revise_save_selector))
        )
        employee_info_revise_save = driver.find_element(By. CSS_SELECTOR, employee_info_revise_save_selector)
        employee_info_revise_save.click()
        print("직원 수정_저장 선택 완료")

        #직원 수정_저장 후 딜레이 2초
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 직원 관리 관련 오류 발생 !!!!!")

employee_admin()
time.sleep(1)


#상품 관리 동작
product_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(5) > li"
product_app_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.w-fit.gap-4.border-b.border-\[--netural-gray-scale-100\] > li:nth-child(2) > button"
product_deactivate_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.w-fit.gap-4.border-b.border-\[--netural-gray-scale-100\] > li:nth-child(3) > button"
product_all_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.w-fit.gap-4.border-b.border-\[--netural-gray-scale-100\] > li:nth-child(1) > button"
product_gx_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(2) > button"
product_pt_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(3) > button"
product_locker_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(4) > button"
product_sports_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(5) > button"
product_default_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.w-full.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(1) > button"
product_add_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > a > button"
product_add_category_selector = "#FC-create-form > div:nth-child(3) > div.flex.flex-col.gap-4 > div:nth-child(2) > div > div"
product_add_category_dropdown_Xpath = "//button[text()='설정된카테고리_01']"
product_add_name_selector = "#productName"
product_add_drop_selector = "#FC-create-form > div:nth-child(4) > div.flex.flex-col.gap-4 > div > div > div.flex.flex-col.gap-2\.5 > div"
product_add_drop_locker_selector = "#LOCKER-create-form > div:nth-child(4) > div.p-5.white-box.flex.flex-col.gap-4 > div > div.flex.flex-col.gap-2\.5 > div"
product_add_drop_sport_selector = "#SPORTS_EQUIPMENT-create-form > div:nth-child(3) > div.p-5.white-box.flex.flex-col.gap-4 > div > div.flex.flex-col.gap-2\.5 > div"
product_add_dropdown_Xpath = "//button[text()='3개월']"
product_add_pause_Xpath = "//p[contains(text(), '정지 설정')]/following::button[1]"
product_add_pausecount_Xpath = "//p[contains(text(), '정지 가능 횟수 제한')]/following::button[1]"
product_add_pause_count_selector = "#reschedulingAvailableCount"
product_add_date_selector = "#reschedulingAvailableDate"
product_add_min_date_Xpath = "//p[contains(text(), '최소 정지 가능일 제한')]/following::button[1]"
product_add_mindate_selector = "#reschedulingMinDate"
product_add_money_selector = "#amount"
product_add_save_selector = "#FC-create-form-btn"
product_add_gx_selector = "#GX"
product_add_pt_selector = "#PT"
product_add_count_gx_selector = "#GX-create-form > div:nth-child(3) > div.flex.flex-col.gap-4 > div:nth-child(2) > ul > li:nth-child(2) > button"
product_add_countAll_selector = "#GX-create-form > div:nth-child(4) > div.flex.flex-col.gap-4 > div:nth-child(1) > ul > li:nth-child(2) > button"
product_add_category_gx_selector = "#GX-create-form > div:nth-child(3) > div.flex.flex-col.gap-4 > div:nth-child(2) > div > div"
product_add_count_pt_selector = "#PT-create-form > div:nth-child(3) > div.flex.flex-col.gap-4 > div:nth-child(2) > ul > li:nth-child(2) > button"
product_add_category_pt_selector = "#PT-create-form > div:nth-child(3) > div.flex.flex-col.gap-4 > div:nth-child(2) > div > div"
product_add_cancel_selector = "#bookingCancelCount"
product_add_usecount_selector = "#useCount"
product_add_save_gx_selector = "#GX-create-form-btn"
product_add_ptsave_selector = "#PT-create-form-btn"
product_add_locker_selector = "#LOCKER"
product_add_category_locker_selector = "#LOCKER-create-form > div:nth-child(3) > div.flex.flex-col.gap-4 > div:nth-child(2) > div > div"
product_add_lockersave_selector = "#LOCKER-create-form-btn"
product_add_sports_selector = "#SPORTS_EQUIPMENT"
product_add_category_sport_selector = "#SPORTS_EQUIPMENT-create-form > div:nth-child(2) > div.flex.flex-col.gap-4 > div > div > div:nth-child(2) > div > div"
product_add_sportssave_selector = "#SPORTS_EQUIPMENT-create-form-btn"
product_revise_selector = "(//a[contains(@href, 'product') and contains(@href, 'update')])[1]"
product_revise_save_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > div > button"
product_del_selector = "(//a[contains(@href, 'product') and contains(@href, 'delete')])[1]"
product_del_save_selector = "body > div.flex.justify-center.items-center.fixed.inset-0.z-50.backdrop-filter.placeholder\:outline-none.focus\:outline-none.cursor-auto.duration-300.h-\[100svh\].rounded-md.bg-black\/60.backdrop-blur-sm > div > div > div > div > div.h-\[3\.125rem\].grid.grid-cols-2.font-medium > form > button"

# "a[hrf*='product/delete?product'e]"
# "a[href*='product/update?product']"
def product_admin():
    global wait_count # 글로벌 변수 선언
    try:
        wait_count += 1
        #상품 관리 선택
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_selector))
        )
        product = driver.find_element(By. CSS_SELECTOR, product_selector)
        product.click()
        print("상품 관리 선택 완료")

        #상품 관리 선택 후 딜레이 2초
        time.sleep(1)

        #APP 노출 상품 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_app_selector))
        )
        product_app = driver.find_element(By. CSS_SELECTOR, product_app_selector)
        product_app.click()
        print("APP 노출 상품 선택 완료")

        #APP 노출 상품 선택 후 딜레이 2초
        time.sleep(1)

        #비활성 상품 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_deactivate_selector))
        )
        product_deactivate = driver.find_element(By. CSS_SELECTOR, product_deactivate_selector)
        product_deactivate.click()
        print("비활성 상품 선택 완료")

        #비활성 상품 탭 선택 후 딜레이 2초
        time.sleep(1)

        #전체 상품 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_all_selector))
        )
        product_all = driver.find_element(By. CSS_SELECTOR, product_all_selector)
        product_all.click()
        print("전체 상품 선택 완료")

        #전체 상품 탭 선택 후 딜레이 2초
        time.sleep(1)

        #그룹 수업 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_gx_selector))
        )
        product_gx = driver.find_element(By. CSS_SELECTOR, product_gx_selector)
        product_gx.click()
        print("그룹 수업 탭 선택 완료")

        #그룹 수업 탭 선택 후 딜레이 2초
        time.sleep(1)

        #개인 레슨 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_pt_selector))
        )
        product_pt = driver.find_element(By. CSS_SELECTOR, product_pt_selector)
        product_pt.click()
        print("개인 레슨 탭 선택 완료")

        #개인 레슨 탭 선택 후 딜레이 2초
        time.sleep(1)

        #락커 상품 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_locker_selector))
        )
        product_locker = driver.find_element(By. CSS_SELECTOR, product_locker_selector)
        product_locker.click()
        print("락커 상품 탭 선택 완료")

        #락커 상품 탭 선택 후 딜레이 2초
        time.sleep(1)

        #운동 용품 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_sports_selector))
        )
        product_sports = driver.find_element(By. CSS_SELECTOR, product_sports_selector)
        product_sports.click()
        print("운동 용품 탭 선택 완료")

        #운동 용품 탭 선택 후 딜레이 2초
        time.sleep(1)

        #회원권 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_default_selector))
        )
        product_default = driver.find_element(By. CSS_SELECTOR, product_default_selector)
        product_default.click()
        print("회원권 탭 선택 완료")

        #회원권 탭 선택 후 딜레이 2초
        time.sleep(1)

        #상품 추가 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_selector))
        )
        product_add = driver.find_element(By. CSS_SELECTOR, product_add_selector)
        product_add.click()
        print("상품 추가 선택 완료")

        #상품 추가 선택 후 딜레이 2초
        time.sleep(1)

        #카테고리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_category_selector))
        )
        product_add_category = driver.find_element(By. CSS_SELECTOR, product_add_category_selector)
        product_add_category.click()
        print("카테고리 드롭다운 선택 완료")

        #드롭다운 선택 후 딜레이 2초
        time.sleep(1)

        #카테고리 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_category_dropdown_Xpath))
        )
        product_add_category_dropdown = driver.find_element(By. XPATH, product_add_category_dropdown_Xpath)
        product_add_category_dropdown.click()
        print("카테고리 선택 완료")

        #회원권 상품 추가_상품명 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_name_selector))
        )
        product_add_name = driver.find_element(By. CSS_SELECTOR, product_add_name_selector)
        product_add_name.clear()
        random_name = generate_random_korean_name()
        product_add_name.send_keys(random_name)
        print("상품명 입력 완료")

        #상품명 입력 후 딜레이 2초
        time.sleep(1)

        #기간 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_drop_selector))
        )
        product_add_drop = driver.find_element(By. CSS_SELECTOR, product_add_drop_selector)
        product_add_drop.click()
        print("기간 드롭다운 선택 완료")

        #드롭다운 선택 후 딜레이 2초
        time.sleep(1)

        #기간 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_dropdown_Xpath))
        )
        product_add_dropdown = driver.find_element(By. XPATH, product_add_dropdown_Xpath)
        product_add_dropdown.click()
        print("3개월 선택 완료")

        #3개월 선택 후 딜레이 2초
        time.sleep(1)

        #정지 설정 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pause_Xpath))
        )
        product_add_pause = driver.find_element(By. XPATH, product_add_pause_Xpath)
        product_add_pause.click()
        print("정지 설정 ON")

        #토글 ON 후 1초
        time.sleep(1)

        #정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_date_selector))
        )
        product_add_date = driver.find_element(By. CSS_SELECTOR, product_add_date_selector)
        product_add_date.clear()
        product_add_date.send_keys("100")
        print("정지 가능일 입력 완료")

        #정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #정지 가능 횟수 제한 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pausecount_Xpath))
        )
        product_add_pausecount = driver.find_element(By. XPATH, product_add_pausecount_Xpath)
        product_add_pausecount.click()
        print("정지 가능 횟수 제한 ON")
        time.sleep(1)

        #정지 가능 횟수 제한 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_pause_count_selector))
        )
        product_add_pause_count = driver.find_element(By. CSS_SELECTOR, product_add_pause_count_selector)
        product_add_pause_count.clear()
        product_add_pause_count.send_keys("10")
        print("가능 제한 횟수 입력 완료")
        time.sleep(1)

        #최소 정지 가능일 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_min_date_Xpath))
        )
        product_add_min_date = driver.find_element(By. XPATH, product_add_min_date_Xpath)
        product_add_min_date.click()
        print("최소 정지 가능일 ON")
        time.sleep(1)

        #최소 정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_mindate_selector))
        )
        product_add_mindate = driver.find_element(By. CSS_SELECTOR, product_add_mindate_selector)
        product_add_mindate.clear()
        product_add_mindate.send_keys("10")
        print("최소 정지 가능일 입력 완료")

        #최소 정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #금액 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_money_selector))
        )
        product_add_money = driver.find_element(By. CSS_SELECTOR, product_add_money_selector)
        product_add_money.clear()
        product_add_money.send_keys("1000000")
        print("금액 입력 완료")

        #금액 입력 후 딜레이 2초
        time.sleep(1)

        #정보 입력 후 저장
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_save_selector))
        )
        product_add_save = driver.find_element(By. CSS_SELECTOR, product_add_save_selector)
        product_add_save.click()
        print("저장 선택 완료")

        #저장 선택 후 딜레이 2초
        time.sleep(1)

        #상품 추가 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_selector))
        )
        product_add = driver.find_element(By. CSS_SELECTOR, product_add_selector)
        product_add.click()
        print("상품 추가 선택 완료")

        #상품 추가 선택 후 딜레이 2초
        time.sleep(1)

        #상품 유형 선택_그룹 수업
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_gx_selector))
        )
        product_add_gx = driver.find_element(By. CSS_SELECTOR, product_add_gx_selector)
        product_add_gx.click()
        print("상품 유형_그룹 수업 선택 완료")

        #상품 유형_그룹 수업 선택 후 딜레이 2초
        time.sleep(1)

        #상품 유형_횟수제 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_count_gx_selector))
        )
        product_add_count_gx = driver.find_element(By. CSS_SELECTOR, product_add_count_gx_selector)
        product_add_count_gx.click()
        print("상품 유형 횟수제 선택 완료")

        #상품 유형_횟수제 선택 후 딜레이 2초
        time.sleep(1)        

        #카테고리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_category_gx_selector))
        )
        product_add_gx_category = driver.find_element(By. CSS_SELECTOR, product_add_category_gx_selector)
        product_add_gx_category.click()
        print("카테고리 드롭다운 선택 완료")

        #드롭다운 선택 후 딜레이 2초
        time.sleep(1)

        #카테고리 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_category_dropdown_Xpath))
        )
        product_add_category_dropdown = driver.find_element(By. XPATH, product_add_category_dropdown_Xpath)
        product_add_category_dropdown.click()
        print("카테고리 선택 완료")        

        #그룹 수업 상품 추가_상품명 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_name_selector))
        )
        product_add_name = driver.find_element(By. CSS_SELECTOR, product_add_name_selector)
        product_add_name.clear()
        random_name = generate_random_korean_name()
        product_add_name.send_keys(random_name)
        print("상품명 입력 완료")

        #상품명 입력 후 딜레이 2초
        time.sleep(1)

        #상품_횟수 종일제 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_countAll_selector))
        )
        product_add_all_count = driver.find_element(By. CSS_SELECTOR, product_add_countAll_selector)
        product_add_all_count.click()
        print("상품 횟수 종일제 선택 완료")

        #상품 유형_종일제 선택 후 딜레이 2초
        time.sleep(1)        

        #이용 횟수 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_usecount_selector))
        )
        product_add_usecount = driver.find_element(By. CSS_SELECTOR, product_add_usecount_selector)
        product_add_usecount.clear
        product_add_usecount.send_keys("10")
        print("이용 횟수 입력 완료")

        #이용 횟수 입력 후 딜레이 2초
        time.sleep(1)

        #취소 가능 횟수 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_cancel_selector))
        )
        product_add_cancel = driver.find_element(By. CSS_SELECTOR, product_add_cancel_selector)
        product_add_cancel.clear
        product_add_cancel.send_keys("10")
        print("취소 가능 횟수 입력 완료")

        #이용 횟수 입력 후 딜레이 2초
        time.sleep(1)

        #정지 설정 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pause_Xpath))
        )
        product_add_pause = driver.find_element(By. XPATH, product_add_pause_Xpath)
        product_add_pause.click()
        print("정지 설정 ON")

        #토글 ON 후 1초
        time.sleep(1)

        #정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_date_selector))
        )
        product_add_date = driver.find_element(By. CSS_SELECTOR, product_add_date_selector)
        product_add_date.clear()
        product_add_date.send_keys("100")
        print("정지 가능일 입력 완료")

        #정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #정지 가능 횟수 제한 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pausecount_Xpath))
        )
        product_add_pausecount = driver.find_element(By. XPATH, product_add_pausecount_Xpath)
        product_add_pausecount.click()
        print("정지 가능 횟수 제한 ON")
        time.sleep(1)

        #정지 가능 횟수 제한 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_pause_count_selector))
        )
        product_add_pause_count = driver.find_element(By. CSS_SELECTOR, product_add_pause_count_selector)
        product_add_pause_count.clear()
        product_add_pause_count.send_keys("10")
        print("가능 제한 횟수 입력 완료")
        time.sleep(1)

        #최소 정지 가능일 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_min_date_Xpath))
        )
        product_add_min_date = driver.find_element(By. XPATH, product_add_min_date_Xpath)
        product_add_min_date.click()
        print("최소 정지 가능일 ON")
        time.sleep(1)

        #최소 정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_mindate_selector))
        )
        product_add_mindate = driver.find_element(By. CSS_SELECTOR, product_add_mindate_selector)
        product_add_mindate.clear()
        product_add_mindate.send_keys("10")
        print("최소 정지 가능일 입력 완료")

        #최소 정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #금액 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_money_selector))
        )
        product_add_money = driver.find_element(By. CSS_SELECTOR, product_add_money_selector)
        product_add_money.clear()
        product_add_money.send_keys("1500000")
        print("금액 입력 완료")

        #금액 입력 후 딜레이 2초
        time.sleep(1)

        #정보 입력 후 저장
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_save_gx_selector))
        )
        product_add_save_gx = driver.find_element(By. CSS_SELECTOR, product_add_save_gx_selector)
        product_add_save_gx.click()
        print("저장 선택 완료")

        #저장 선택 후 딜레이 2초
        time.sleep(1)

        #상품 추가 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_selector))
        )
        product_add = driver.find_element(By. CSS_SELECTOR, product_add_selector)
        product_add.click()
        print("상품 추가 선택 완료")

        #상품 추가 선택 후 딜레이 2초
        time.sleep(1)

        #상품 유형 선택_개인 레슨
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_pt_selector))
        )
        product_add_pt = driver.find_element(By. CSS_SELECTOR, product_add_pt_selector)
        product_add_pt.click()
        print("상품 유형_개인 레슨 선택 완료")

        #상품 유형_개인 레슨 선택 후 딜레이 2초
        time.sleep(1)

        #상품 유형_횟수제 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_count_pt_selector))
        )
        product_add_count_pt = driver.find_element(By. CSS_SELECTOR, product_add_count_pt_selector)
        product_add_count_pt.click()
        print("상품 유형 횟수제 선택 완료")

        #상품 유형_횟수제 선택 후 딜레이 2초
        time.sleep(1)        

        #카테고리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_category_pt_selector))
        )
        product_add_pt_category = driver.find_element(By. CSS_SELECTOR, product_add_category_pt_selector)
        product_add_pt_category.click()
        print("카테고리 드롭다운 선택 완료")

        #드롭다운 선택 후 딜레이 2초
        time.sleep(1)

        #카테고리 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_category_dropdown_Xpath))
        )
        product_add_category_dropdown = driver.find_element(By. XPATH, product_add_category_dropdown_Xpath)
        product_add_category_dropdown.click()
        print("카테고리 선택 완료")        

        #개인 레슨 상품 추가_상품명 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_name_selector))
        )
        product_add_name = driver.find_element(By. CSS_SELECTOR, product_add_name_selector)
        product_add_name.clear()
        random_name = generate_random_korean_name()
        product_add_name.send_keys(random_name)
        print("상품명 입력 완료")

        #상품명 입력 후 딜레이 2초
        time.sleep(1)

        #이용 횟수 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_usecount_selector))
        )
        product_add_usecount = driver.find_element(By. CSS_SELECTOR, product_add_usecount_selector)
        product_add_usecount.clear
        product_add_usecount.send_keys("10")
        print("이용 횟수 입력 완료")

        #이용 횟수 입력 후 딜레이 2초
        time.sleep(1)

        #정지 설정 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pause_Xpath))
        )
        product_add_pause = driver.find_element(By. XPATH, product_add_pause_Xpath)
        product_add_pause.click()
        print("정지 설정 ON")

        #토글 ON 후 1초
        time.sleep(1)

        #정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_date_selector))
        )
        product_add_date = driver.find_element(By. CSS_SELECTOR, product_add_date_selector)
        product_add_date.clear()
        product_add_date.send_keys("100")
        print("정지 가능일 입력 완료")

        #정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #정지 가능 횟수 제한 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pausecount_Xpath))
        )
        product_add_pausecount = driver.find_element(By. XPATH, product_add_pausecount_Xpath)
        product_add_pausecount.click()
        print("정지 가능 횟수 제한 ON")
        time.sleep(1)

        #정지 가능 횟수 제한 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_pause_count_selector))
        )
        product_add_pause_count = driver.find_element(By. CSS_SELECTOR, product_add_pause_count_selector)
        product_add_pause_count.clear()
        product_add_pause_count.send_keys("10")
        print("가능 제한 횟수 입력 완료")
        time.sleep(1)

        #최소 정지 가능일 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_min_date_Xpath))
        )
        product_add_min_date = driver.find_element(By. XPATH, product_add_min_date_Xpath)
        product_add_min_date.click()
        print("최소 정지 가능일 ON")
        time.sleep(1)

        #최소 정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_mindate_selector))
        )
        product_add_mindate = driver.find_element(By. CSS_SELECTOR, product_add_mindate_selector)
        product_add_mindate.clear()
        product_add_mindate.send_keys("10")
        print("최소 정지 가능일 입력 완료")

        #최소 정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #금액 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_money_selector))
        )
        product_add_money = driver.find_element(By. CSS_SELECTOR, product_add_money_selector)
        product_add_money.clear()
        product_add_money.send_keys("1500000")
        print("금액 입력 완료")

        #금액 입력 후 딜레이 2초
        time.sleep(1)

        #정보 입력 후 저장
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_ptsave_selector))
        )
        product_add_save_pt = driver.find_element(By. CSS_SELECTOR, product_add_ptsave_selector)
        product_add_save_pt.click()
        print("저장 선택 완료")

        #저장 선택 후 딜레이 2초
        time.sleep(1)

        #상품 추가 선택_3
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_selector))
        )
        product_add = driver.find_element(By. CSS_SELECTOR, product_add_selector)
        product_add.click()
        print("상품 추가 선택 완료")

        #상품 추가 선택 후 딜레이 2초
        time.sleep(1)

        #상품 유형 선택_락커 상품
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_locker_selector))
        )
        product_add_locker = driver.find_element(By. CSS_SELECTOR, product_add_locker_selector)
        product_add_locker.click()
        print("상품 유형_락커 상품 선택 완료")

        #상품 유형_개인 레슨 선택 후 딜레이 2초
        time.sleep(1)

        #카테고리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_category_locker_selector))
        )
        product_add_locker_category = driver.find_element(By. CSS_SELECTOR, product_add_category_locker_selector)
        product_add_locker_category.click()
        print("카테고리 드롭다운 선택 완료")

        #드롭다운 선택 후 딜레이 2초
        time.sleep(1)

        #카테고리 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_category_dropdown_Xpath))
        )
        product_add_category_dropdown = driver.find_element(By. XPATH, product_add_category_dropdown_Xpath)
        product_add_category_dropdown.click()
        print("카테고리 선택 완료")      

        #락커 상품 상품 추가_상품명 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_name_selector))
        )
        product_add_name = driver.find_element(By. CSS_SELECTOR, product_add_name_selector)
        product_add_name.clear()
        random_name = generate_random_korean_name()
        product_add_name.send_keys(random_name)
        print("상품명 입력 완료")

        #상품명 입력 후 딜레이 2초
        time.sleep(1)

        #기간 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_drop_locker_selector))
        )
        product_add_drop_locker = driver.find_element(By. CSS_SELECTOR, product_add_drop_locker_selector)
        product_add_drop_locker.click()
        print("기간 드롭다운 선택 완료")

        #드롭다운 선택 후 딜레이 2초
        time.sleep(1)

        #기간 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_dropdown_Xpath))
        )
        product_add_dropdown = driver.find_element(By. XPATH, product_add_dropdown_Xpath)
        product_add_dropdown.click()
        print("3개월 선택 완료")

        #3개월 선택 후 딜레이 2초
        time.sleep(1)

        #정지 설정 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pause_Xpath))
        )
        product_add_pause = driver.find_element(By. XPATH, product_add_pause_Xpath)
        product_add_pause.click()
        print("정지 설정 ON")

        #토글 ON 후 1초
        time.sleep(1)

        #정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_date_selector))
        )
        product_add_date = driver.find_element(By. CSS_SELECTOR, product_add_date_selector)
        product_add_date.clear()
        product_add_date.send_keys("100")
        print("정지 가능일 입력 완료")

        #정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #정지 가능 횟수 제한 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pausecount_Xpath))
        )
        product_add_pausecount = driver.find_element(By. XPATH, product_add_pausecount_Xpath)
        product_add_pausecount.click()
        print("정지 가능 횟수 제한 ON")
        time.sleep(1)

        #정지 가능 횟수 제한 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_pause_count_selector))
        )
        product_add_pause_count = driver.find_element(By. CSS_SELECTOR, product_add_pause_count_selector)
        product_add_pause_count.clear()
        product_add_pause_count.send_keys("10")
        print("가능 제한 횟수 입력 완료")
        time.sleep(1)

        #최소 정지 가능일 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_min_date_Xpath))
        )
        product_add_min_date = driver.find_element(By. XPATH, product_add_min_date_Xpath)
        product_add_min_date.click()
        print("최소 정지 가능일 ON")
        time.sleep(1)

        #최소 정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_mindate_selector))
        )
        product_add_mindate = driver.find_element(By. CSS_SELECTOR, product_add_mindate_selector)
        product_add_mindate.clear()
        product_add_mindate.send_keys("10")
        print("최소 정지 가능일 입력 완료")

        #최소 정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #금액 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_money_selector))
        )
        product_add_money = driver.find_element(By. CSS_SELECTOR, product_add_money_selector)
        product_add_money.clear()
        product_add_money.send_keys("1500000")
        print("금액 입력 완료")

        #금액 입력 후 딜레이 2초
        time.sleep(1)

        #정보 입력 후 저장
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_lockersave_selector))
        )
        product_add_save_locker = driver.find_element(By. CSS_SELECTOR, product_add_lockersave_selector)
        product_add_save_locker.click()
        print("저장 선택 완료")

        #저장 완료 후 딜레이 2초
        time.sleep(1)

        #상품 추가 선택_4
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_selector))
        )
        product_add = driver.find_element(By. CSS_SELECTOR, product_add_selector)
        product_add.click()
        print("상품 추가 선택 완료")

        #상품 추가 선택 후 딜레이 2초
        time.sleep(1)

        #상품 유형 선택_락커 상품
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_sports_selector))
        )
        product_add_sports = driver.find_element(By. CSS_SELECTOR, product_add_sports_selector)
        product_add_sports.click()
        print("상품 유형_운동 용품 선택 완료")

        #상품 유형_운동 용품 선택 후 딜레이 2초
        time.sleep(1)

        #카테고리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_category_sport_selector))
        )
        product_add_sport_category = driver.find_element(By. CSS_SELECTOR, product_add_category_sport_selector)
        product_add_sport_category.click()
        print("카테고리 드롭다운 선택 완료")

        #드롭다운 선택 후 딜레이 2초
        time.sleep(1)

        #카테고리 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_category_dropdown_Xpath))
        )
        product_add_category_dropdown = driver.find_element(By. XPATH, product_add_category_dropdown_Xpath)
        product_add_category_dropdown.click()
        print("카테고리 선택 완료")

        #운동 용품 추가_상품명 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_name_selector))
        )
        product_add_name = driver.find_element(By. CSS_SELECTOR, product_add_name_selector)
        product_add_name.clear()
        random_name = generate_random_korean_name()
        product_add_name.send_keys(random_name)
        print("상품명 입력 완료")

        #상품명 입력 후 딜레이 2초
        time.sleep(1)

        #기간 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_drop_sport_selector))
        )
        product_add_drop_sport = driver.find_element(By. CSS_SELECTOR, product_add_drop_sport_selector)
        product_add_drop_sport.click()
        print("기간 드롭다운 선택 완료")

        #드롭다운 선택 후 딜레이 2초
        time.sleep(1)

        #기간 선택_2
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_dropdown_Xpath))
        )
        product_add_dropdown = driver.find_element(By. XPATH, product_add_dropdown_Xpath)
        product_add_dropdown.click()
        print("3개월 선택 완료")

        #3개월 선택 후 딜레이 2초
        time.sleep(1)

        #정지 설정 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pause_Xpath))
        )
        product_add_pause = driver.find_element(By. XPATH, product_add_pause_Xpath)
        product_add_pause.click()
        print("정지 설정 ON")

        #토글 ON 후 1초
        time.sleep(1)

        #정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_date_selector))
        )
        product_add_date = driver.find_element(By. CSS_SELECTOR, product_add_date_selector)
        product_add_date.clear()
        product_add_date.send_keys("100")
        print("정지 가능일 입력 완료")

        #정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #정지 가능 횟수 제한 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_pausecount_Xpath))
        )
        product_add_pausecount = driver.find_element(By. XPATH, product_add_pausecount_Xpath)
        product_add_pausecount.click()
        print("정지 가능 횟수 제한 ON")
        time.sleep(1)

        #정지 가능 횟수 제한 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_pause_count_selector))
        )
        product_add_pause_count = driver.find_element(By. CSS_SELECTOR, product_add_pause_count_selector)
        product_add_pause_count.clear()
        product_add_pause_count.send_keys("10")
        print("가능 제한 횟수 입력 완료")
        time.sleep(1)

        #최소 정지 가능일 ON
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_add_min_date_Xpath))
        )
        product_add_min_date = driver.find_element(By. XPATH, product_add_min_date_Xpath)
        product_add_min_date.click()
        print("최소 정지 가능일 ON")
        time.sleep(1)

        #최소 정지 가능일 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_mindate_selector))
        )
        product_add_mindate = driver.find_element(By. CSS_SELECTOR, product_add_mindate_selector)
        product_add_mindate.clear()
        product_add_mindate.send_keys("10")
        print("최소 정지 가능일 입력 완료")

        #최소 정지 가능일 입력 후 딜레이 2초
        time.sleep(1)

        #금액 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_money_selector))
        )
        product_add_money = driver.find_element(By. CSS_SELECTOR, product_add_money_selector)
        product_add_money.clear()
        product_add_money.send_keys("500000")
        print("금액 입력 완료")

        #금액 입력 후 딜레이 2초
        time.sleep(1)

        #정보 입력 후 저장
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_add_sportssave_selector))
        )
        product_add_save_sports = driver.find_element(By. CSS_SELECTOR, product_add_sportssave_selector)
        product_add_save_sports.click()
        print("저장 선택 완료")

        #저장 후 딜레이 2초
        time.sleep(1)

        #회원권 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_default_selector))
        )
        product_default = driver.find_element(By. CSS_SELECTOR, product_default_selector)
        product_default.click()
        print("회원권 탭 선택 완료")

        #회원권 탭 선택 후 딜레이 2초
        time.sleep(1)

        #상품 수정 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_revise_selector))
        )
        product_revise = driver.find_element(By. XPATH, product_revise_selector)
        product_revise.click()
        print("상품 수정 선택 완료")

        #상품 수정 선택 후 딜레이 2초
        time.sleep(1)

        #상품 수정_저장
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_revise_save_selector))
        )
        product_revise_save = driver.find_element(By. CSS_SELECTOR, product_revise_save_selector)
        product_revise_save.click()
        print("상품 수정 저장 완료")

        #상품 수정 저장 후 딜레이 2초
        time.sleep(1)

        #상품 삭제 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, product_del_selector))
        )
        product_del = driver.find_element(By. XPATH, product_del_selector)
        product_del.click()
        print("상품 삭제 선택 완료")

        #상품 삭제 선택 후 딜레이 2초
        time.sleep(1)

        #상품 삭제_삭제하기 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, product_del_save_selector))
        )
        product_del_save = driver.find_element(By. CSS_SELECTOR, product_del_save_selector)
        product_del_save.click()
        print("상품 삭제 완료")

        #상품 삭제 후 딜레이 2초
        time.sleep(1)
     
    except (NoSuchElementException, TimeoutException):
        print("!!!!! 상품 관리 관련 오류 발생 !!!!!")

product_admin()
time.sleep(1)


#락커 관리 동작
locker_selector ="body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(6) > li"
locker_assingned_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.flex.justify-between.pt-5.px-10.pb-2\.5 > ul > li:nth-child(1) > button"
locker_unassigned_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.flex.justify-between.pt-5.px-10.pb-2\.5 > ul > li:nth-child(2) > button"
locker_member_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.flex-1.px-10.flex.flex-col.mb-8 > table > tbody > tr:nth-child(1)"
locker_setting_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div.flex.justify-between.pt-5.px-10.pb-2\.5 > ul > li:nth-child(3) > button"



def locker_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #락커 관리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, locker_selector))
        )
        locker = driver.find_element(By. CSS_SELECTOR, locker_selector)
        locker.click()
        print("락커 관리 선택 완료")

        #락커 관리 선택 후 딜레이 2초
        time.sleep(1)

        #락커 관리 _ 미배정자 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, locker_unassigned_selector))
        )
        locker_unassigned = driver.find_element(By. CSS_SELECTOR, locker_unassigned_selector)
        locker_unassigned.click()
        print("미배정자 선택 완료")

        #락커 관리 _ 미배정자 선택 후 딜레이 2초
        time.sleep(1)

        #락커 관리 _ 미배정자 _ 정보 조회
        wait_count += 2
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, locker_member_selector))
        )
        locker_member = driver.find_element(By. CSS_SELECTOR, locker_member_selector)
        locker_member.click()
        print("미배정자_정보 조회 선택 완료")

        #정보 조회 선택 후 딜레이 2초
        time.sleep(1)

        #이전 화면 이동
        driver.back()
        print("이전 페이지 이동 완료")
        time.sleep(1)

        #락커 관리 _ 락커 설정 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, locker_setting_selector))
        )
        locker_setting = driver.find_element(By. CSS_SELECTOR, locker_setting_selector)
        locker_setting.click()
        print("락커 설정 선택 완료")

        #락커 관리 _ 락커 설정 선택 후 딜레이 2초
        time.sleep(1)

        #락커 관리 _ 배정 현황 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, locker_assingned_selector))
        )
        locker_assingned = driver.find_element(By. CSS_SELECTOR, locker_assingned_selector)
        locker_assingned.click()
        print("배정 현황 선택 완료")

        #락커 관리 _ 락커 설정 선택 후 딜레이 2초
        time.sleep(1)                

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 락커 관리 관련 오류 발생 !!!!!")

locker_admin()
time.sleep(1)


#출석 동작
attendance_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(7) > li"
attendance_PT_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.pb-\[2\.5rem\].flex-grow.flex.flex-col.gap-5 > div.h-\[3\.125rem\].flex.justify-end.items-center > ul > li:nth-child(2) > button"
attendance_GX_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.pb-\[2\.5rem\].flex-grow.flex.flex-col.gap-5 > div.h-\[3\.125rem\].flex.justify-end.items-center > ul > li:nth-child(3) > button"
attendance_counselings_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.pb-\[2\.5rem\].flex-grow.flex.flex-col.gap-5 > div.h-\[3\.125rem\].flex.justify-end.items-center > ul > li:nth-child(4) > button"


def attendance_admin():
    global wait_count
    try:
        #출석 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, attendance_selector))
        )
        attendance = driver.find_element(By. CSS_SELECTOR, attendance_selector)
        attendance.click()
        print("출석 선택 완료")

        #출석 선택 완료 후 딜레이 2초
        time.sleep(1)

        #개인 레슨 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, attendance_PT_selector))
        )
        attendance_PT = driver.find_element(By. CSS_SELECTOR, attendance_PT_selector)
        attendance_PT.click()
        print("개인 레슨 탭 선택 완료")

        #개인 레슨 탭 선택 완료 후 딜레이 2초
        time.sleep(1)

        #그룹 수업 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, attendance_GX_selector))
        )
        attendance_GX = driver.find_element(By. CSS_SELECTOR, attendance_GX_selector)
        attendance_GX.click()
        print("그룹 수업 탭 선택 완료")

        #그룹 수업 탭 선택 완료 후 딜레이 2초
        time.sleep(1)

        #상담 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, attendance_counselings_selector))
        )
        attendance_counselings = driver.find_element(By. CSS_SELECTOR, attendance_counselings_selector)
        attendance_counselings.click()
        print("상담 탭 선택 완료")

        #상담 탭 선택 완료 후 딜레이 2초
        time.sleep(1)
    
    except (NoSuchElementException, TimeoutException):
        print("!!!!! 출석 관련 오류 발생 !!!!!")

attendance_admin()
time.sleep(1)
        
#스케줄 관리 동작
schedule_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(8) > li"
schedule_add_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div > div.max-h-\[calc\(100vh-12\.5rem\)\].border.border-\[--netural-gray-scale-100\].rounded-2xl.z-0.rbc-calendar > div > div.rbc-time-content > div:nth-child(2) > div.rbc-events-container"
schedule_add_re_selector = "#taskStartTime"
schedule_add_min_selector = "#create-schedule-form > div:nth-child(4) > div > div.flex.flex-col.gap-2 > div > button:nth-child(2)"
schedule_add_member_selector = "#create-schedule-form > div.flex.gap-4.px-5.flex-1 > div > div.p-4.flex.flex-col.gap-4.max-h-\[15\.625rem\].overflow-y-auto.border.border-\[--netural-gray-scale-100\].rounded-2xl > div:nth-child(1)"
schedule_add_member_product_selector = "#create-schedule-form article:first-of-type button"
schedule_add_save_selector = "body > div.flex.justify-end.fixed.inset-0.z-50.outline-none.focus\:outline-none.bg-black\/60.cursor-auto.backdrop-filter.backdrop-blur-sm.duration-300 > div > div > div.flex-auto.overflow-y-auto > div > button"
schedule_add_search_selector = "#search-member"



def schedule_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #스케줄 관리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, schedule_selector))
        )
        schedule = driver.find_element(By. CSS_SELECTOR, schedule_selector)
        schedule.click()
        print("스케줄 관리 선택 완료")

        #스케줄 관리 선택 후 딜레이 2초
        time.sleep(1) 

        #스케줄 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, schedule_add_selector))
        )
        schedule_add = driver.find_element(By. CSS_SELECTOR, schedule_add_selector)
        schedule_add.click()
        print("스케줄 선택 완료")

        #스케줄 선택 후 딜레이 2초
        time.sleep(1)

        #스케줄 일시 수정
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, schedule_add_re_selector))
        )
        schedule_add_re = driver.find_element(By. CSS_SELECTOR, schedule_add_re_selector)
        schedule_add_re.click()
        print("스케줄 선택 완료")

        #스케줄 선택 후 딜레이 2초
        time.sleep(1)        

        #수업 시간 입력 동작
        #방향키 아래 (오후 선택)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        
        time.sleep(1)

        #탭 동작 (시간 입력을 위해)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)

        #수업 시작 시간 입력
        actions.send_keys("1400").perform()
        print("수업 시작 시간 입력 완료")

        time.sleep(1)

        #30분 진행 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, schedule_add_min_selector))
        )
        schedule_add_min = driver.find_element(By. CSS_SELECTOR, schedule_add_min_selector)
        schedule_add_min.click()
        print("30분 진행 선택 완료")

        #회원 검색
        wait_count += 1  # WebDriverWait 호출 시 카운터 증가
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, schedule_add_search_selector))
        )
        member_search = driver.find_element(By.CSS_SELECTOR, schedule_add_search_selector)
        member_search.clear()
        member_search.send_keys("황성민")
        member_search.send_keys(Keys.RETURN)
        print("회원 검색 완료")

        #회원 검색 후 딜레이 1초
        time.sleep(1)

        #일정 추가_회원 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, schedule_add_member_selector))
        )
        schedule_add_member = driver.find_element(By. CSS_SELECTOR, schedule_add_member_selector)
        schedule_add_member.click()
        print("회원 선택 완료")

        #일정 추가_ 회원 선택 후 딜레이 2초
        time.sleep(1)

        #회원 선택 후 상품 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, schedule_add_member_product_selector))
        )
        schedule_add_member_product = driver.find_element(By. CSS_SELECTOR, schedule_add_member_product_selector)
        schedule_add_member_product.click()
        print("이용권 선택 완료")

        #회원 선택 후 딜레이 2초
        time.sleep(1)

        #일정 저장
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, schedule_add_save_selector))
        )
        schedule_add_save = driver.find_element(By. CSS_SELECTOR, schedule_add_save_selector)
        schedule_add_save.click()
        print("일정 저장 완료")

        #일정 저장 후 딜레이 2초
        time.sleep(1)


    except (NoSuchElementException, TimeoutException):
        print("!!!!! 스케줄 관리 관련 오류 발생 !!!!!")

schedule_admin()
time.sleep(1)


#OT 신청 관리 동작
OT_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(9) > li"

def OT_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #OT 신청 관리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, OT_selector))
        )
        OT = driver.find_element(By. CSS_SELECTOR, OT_selector)
        OT.click()
        print("OT 신청 관리 선택 완료")
        
        #OT 신청 관리 선택 후 딜레이 2초
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! OT 신청 관리 관련 오류 발생 !!!!!")

OT_admin()
time.sleep(1)


#개인 레슨 관리 동작
PT_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(10) > li"

def PT_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #개인 레슨 관리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, PT_selector))
        )
        PT = driver.find_element(By. CSS_SELECTOR, PT_selector)
        PT.click()
        print("개인 레슨 관리 선택 완료")
        
        #개인 레슨 관리 선택 후 딜레이 2초
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 개인 레슨 관리 관련 오류 발생 !!!!!")

PT_admin()
time.sleep(1)

#그룹 수업 관리 동작
GX_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(11) > li"
GX_reservation_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(1) > button > p"
GX_class_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(2) > button > p"
GX_class_all_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(3) > button"
GX_class_deactivate_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(2) > button"
GX_class_active_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.flex.justify-between.items-center.pt-5.pb-2\.5 > ul.flex.h-10.p-\[0\.3125rem\].gap-\[0\.875rem\].bg-\[--netural-gray-scale-100\].rounded-lg > li:nth-child(1) > button"
GX_class_add_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > a > button"
GX_Class_name_selector = "#className"
GX_class_category_selector = "#create > div:nth-child(2) > section > div:nth-child(2) > div.relative.inline-block.w-full.max-w-\[21\.375rem\]"
GX_clsas_category_name_Xpath = "//button[text()='설정된카테고리_01']"
GX_Class_employee_selector = "#create > div:nth-child(2) > section > div:nth-child(3) > div.relative.inline-block.w-full.max-w-\[21\.375rem\]"
GX_Class_employee_name_Xpath = "//button[text()='황성민']"
GX_Class_start_day_selector = "#create > div:nth-child(2) > section > div:nth-child(4) > div.flex.w-full.items-center.justify-end > div > div > label:nth-child(1)"
GX_Class_start_time_selector = "#create > div:nth-child(2) > section > div:nth-child(5) > div.flex.w-full.items-center.justify-end > div > div > label:nth-child(1)"
GX_Class_end_time_selector = "#create > div:nth-child(2) > section > div:nth-child(5) > div.flex.w-full.items-center.justify-end > div > div > label:nth-child(3)"
GX_class_maxmember_selector = "#maxMember"
GX_Class_minmember_selector = "#minMember"
GX_Class_save_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > footer > button"
GX_Class_update_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.grid.grid-cols-1.gap-5.pt-5.pb-\[1\.875rem\].xl\:grid-cols-3.lg\:grid-cols-2 > div:nth-child(1) > div.flex.flex-col.gap-2.pb-4 > div.flex.justify-between.items-center > div > a:nth-child(1) > svg"
GX_Class_del_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.grid.grid-cols-1.gap-5.pt-5.pb-\[1\.875rem\].xl\:grid-cols-3.lg\:grid-cols-2 > div:nth-child(1) > div.flex.flex-col.gap-2.pb-4 > div.flex.justify-between.items-center > div > a:nth-child(2) > svg"
GX_Class_copy_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.grid.grid-cols-1.gap-5.pt-5.pb-\[1\.875rem\].xl\:grid-cols-3.lg\:grid-cols-2 > div:nth-child(1) > div.flex.flex-col.gap-2.pb-4 > div.flex.justify-between.items-center > div > a:nth-child(3) > svg"
GX_Class_del_con_selector = "body > div.flex.justify-center.items-center.fixed.inset-0.z-50.backdrop-filter.placeholder\:outline-none.focus\:outline-none.cursor-auto.duration-300.h-\[100svh\].rounded-md.bg-black\/60.backdrop-blur-sm > div > div > div > div > div.h-\[3\.125rem\].grid.grid-cols-2.font-medium > form > button"
GX_Class_todays_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > div > div.flex.justify-between.items-center.pt-5.pb-2\.5 > ul > li:nth-child(3) > button > p"


def GX_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #그룹 수업 관리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_selector))
        )
        GX = driver.find_element(By. CSS_SELECTOR, GX_selector)
        GX.click()
        print("그룹 수업 관리 선택 완료")
        
        #그룹 수업 관리 선택 후 딜레이 2초
        time.sleep(1)

        #그룹 수업 관리 수업 목록 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_class_selector))
        )
        GX_class = driver.find_element(By. CSS_SELECTOR, GX_class_selector)
        GX_class.click()
        print("수업 목록 탭 선택 완료")

        #수업 목록 탭 선택 후 딜레이 2초
        time.sleep(1)

        #앱 미노출 수업 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_class_deactivate_selector))
        )
        GX_class_deactivate = driver.find_element(By. CSS_SELECTOR, GX_class_deactivate_selector)
        GX_class_deactivate.click()
        print("앱 미노출 수업 선택 완료")

        time.sleep(1)

        #전체 수업 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_class_all_selector))
        )
        GX_class_all = driver.find_element(By. CSS_SELECTOR, GX_class_all_selector)
        GX_class_all.click()
        print("전체 수업 선택 완료")

        time.sleep(1)

        #앱 노출 수업 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_class_active_selector))
        )
        GX_class_active = driver.find_element(By. CSS_SELECTOR, GX_class_active_selector)
        GX_class_active.click()
        print("앱 노출 수업 선택 완료")

        time.sleep(1)

        #수업 추가 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_class_add_selector))
        )
        GX_class_add = driver.find_element(By. CSS_SELECTOR, GX_class_add_selector)
        GX_class_add.click()
        print("수업 추가 선택 완료")

        time.sleep(1)

        #수업 추가_수업명 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_name_selector))
        )
        GX_Class_name = driver.find_element(By. CSS_SELECTOR, GX_Class_name_selector)
        GX_Class_name.clear()
        random_name = generate_random_korean_name()
        GX_Class_name.send_keys(random_name)
        print("수업명 입력 완료")

        time.sleep(1)

        #수업 카테고리 드롭 다운
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_class_category_selector))
        )
        GX_Class_category = driver.find_element(By. CSS_SELECTOR, GX_class_category_selector)
        GX_Class_category.click()
        print("수업 카테고리 드롭 다운 선택 완료")

        time.sleep(1)

        #수업 카테고리 선택 완료
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, GX_clsas_category_name_Xpath))
        )
        GX_Class_category_name = driver.find_element(By. XPATH, GX_clsas_category_name_Xpath)
        GX_Class_category_name.click()
        print("수업 카테고리 선택 완료")

        time.sleep(1)

        #담당 강사 드롭 다운
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_employee_selector))
        )
        GX_Class_employee = driver.find_element(By. CSS_SELECTOR, GX_Class_employee_selector)
        GX_Class_employee.click()
        print("담당 강사 드롭 다운 선택 완료")

        time.sleep(1)

        #담당 강사 선택 완료
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. XPATH, GX_Class_employee_name_Xpath))
        )
        GX_Class_employee_name = driver.find_element(By. XPATH, GX_Class_employee_name_Xpath)
        GX_Class_employee_name.click()
        print("담당 강사 선택 완료")

        time.sleep(1)

        #수업 진행 기간 입력 동작
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_start_day_selector))
        )
        GX_Class_start_day = driver.find_element(By. CSS_SELECTOR, GX_Class_start_day_selector)
        GX_Class_start_day.click()

        time.sleep(1)

        #수업 진행 기간 입력
        actions = ActionChains(driver)
        actions.send_keys("20201020").perform()
        print("수업 진행 기간 시작일 입력 완료")

        time.sleep(1)
    

        #수업 시간 입력 동작
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_start_time_selector))
        )
        GX_Class_start_time = driver.find_element(By. CSS_SELECTOR, GX_Class_start_time_selector)
        GX_Class_start_time.click()

        time.sleep(1)

        #수업 시간 입력 동작
        #방향키 위 (오전 선택)
        actions.send_keys(Keys.ARROW_UP).perform()
        
        time.sleep(1)

        #탭 동작 (시간 입력을 위해)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)

        #수업 시작 시간 입력
        actions.send_keys("1030").perform()
        print("수업 시작 시간 입력 완료")

        time.sleep(1)

        #수업 종료 입력 동작
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_end_time_selector))
        )
        GX_Class_end_time = driver.find_element(By. CSS_SELECTOR, GX_Class_end_time_selector)
        GX_Class_end_time.click()

        time.sleep(1)

        #수업 시간 입력 동작
        #방향키 위 (오전 선택)
        actions.send_keys(Keys.ARROW_UP).perform()
        
        time.sleep(1)

        #탭 동작 (시간 입력을 위해)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)

        #수업 종료 시간 입력
        actions.send_keys("1130").perform()
        print("수업 종료 시간 입력 완료")

        time.sleep(1)

        #정원 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_class_maxmember_selector))
        )
        GX_class_maxmember = driver.find_element(By. CSS_SELECTOR, GX_class_maxmember_selector)
        GX_class_maxmember.clear()
        GX_class_maxmember.send_keys(10)
        print("정원 입력 완료")

        #최소 인원 입력
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_minmember_selector))
        )
        GX_class_minmember = driver.find_element(By. CSS_SELECTOR, GX_Class_minmember_selector)
        GX_class_minmember.clear()
        GX_class_minmember.send_keys(1)
        print("최소 인원 입력 완료")

        time.sleep(1)

        #수업 저장
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_save_selector))
        )
        GX_Class_save = driver.find_element(By. CSS_SELECTOR, GX_Class_save_selector)
        GX_Class_save.click()
        print("수업 저장 완료")

        time.sleep(1)

        #수업 수정
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_update_selector))
        )
        GX_Class_update = driver.find_element(By. CSS_SELECTOR , GX_Class_update_selector)
        GX_Class_update.click()
        print("수업 수정 선택 완료")

        time.sleep(1)

        #수업 수정_저장
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_save_selector))
        )
        GX_Class_save = driver.find_element(By. CSS_SELECTOR, GX_Class_save_selector)
        GX_Class_save.click()
        print("수업 수정_저장 완료")

        time.sleep(1)

        #수업 삭제
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_del_selector))
        )
        GX_Class_del = driver.find_element(By. CSS_SELECTOR, GX_Class_del_selector)
        GX_Class_del.click()
        print("수업 삭제 선택 완료")

        time.sleep(1)
        
        #수업 삭제 팝업 _ 수업 삭제
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_del_con_selector))
        )
        GX_Class_del_con = driver.find_element(By. CSS_SELECTOR, GX_Class_del_con_selector)
        GX_Class_del_con.click()
        print("수업 삭제 완료")

        time.sleep(1)

        #수업 복사 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_copy_selector))
        )
        GX_Class_copy = driver.find_element(By. CSS_SELECTOR, GX_Class_copy_selector)
        GX_Class_copy.click()
        print("수업 복사 선택 완료")

        time.sleep(1)

        #수업 복사 완료
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_save_selector))
        )
        GX_Class_save = driver.find_element(By. CSS_SELECTOR, GX_Class_save_selector)
        GX_Class_save.click()
        print("수업 복사 완료")

        time.sleep(1)

        #그룹 수업 관리 오늘의 운동 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_Class_todays_selector))
        )
        GX_todays = driver.find_element(By. CSS_SELECTOR, GX_Class_todays_selector)
        GX_todays.click()
        print("오늘의 운동 탭 선택 완료")

        #예약 내역 탭 선택 후 딜레이 2초
        time.sleep(1)

        #그룹 수업 관리 예약 내역 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, GX_reservation_selector))
        )
        GX_reservation = driver.find_element(By. CSS_SELECTOR, GX_reservation_selector)
        GX_reservation.click()
        print("예약 내역 탭 선택 완료")

        #예약 내역 탭 선택 후 딜레이 2초
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 그룹 수업 관리 관련 오류 발생 !!!!!")

GX_admin()
time.sleep(1)

#계약서 관리
contract_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(13) > li"

def contract_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #계약서 관리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, contract_selector))
        )
        contract = driver.find_element(By. CSS_SELECTOR, contract_selector)
        contract.click()
        print("계약서 관리 선택 완료")

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 계약서 관리 관련 오류 발생 !!!!!")

contract_admin()
time.sleep(1)

#상담 관리 동작
visitor_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(13) > li"

def visitor_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #상담 관리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, visitor_selector))
        )
        visitor = driver.find_element(By. CSS_SELECTOR, visitor_selector)
        visitor.click()
        print("상담 관리 선택 완료")

        #상담 관리 선택 후 딜레이 2초
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 상담 관리 관련 오류 발생 !!!!!")

visitor_admin()
time.sleep(1)

#기타 매출 관리 동작
ect_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(14) > li"

def ect_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #기타 매출 관리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, ect_selector))
        )
        ect = driver.find_element(By. CSS_SELECTOR, ect_selector)
        ect.click()
        print("기타 매출 관리 선택 완료")

        #상담 관리 선택 후 딜레이 2초
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 기타 매출 관리 관련 오류 발생 !!!!!")

ect_admin()
time.sleep(1)

#통계 관리
statistics_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > ul > div > div:nth-child(2) > details > a:nth-child(15) > li"
statistics_sales_selector = "body > div.w-screen.h-\[100svh\].flex.overflow-hidden.bg-\[var\(--netural-gray-scale-white\)\] > div > div > div.px-10.sticky.top-0.flex.flex-col.items-start.pt-5.pb-2.bg-\[--netural-gray-scale-white\].z-10 > ul > button:nth-child(1) > li > h4"
statistics_payment_selector =  "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div.px-10.sticky.top-16.flex.flex-col.items-start.pt-4.bg-\[--netural-gray-scale-white\].z-10 > ul > li:nth-child(2) > button"
statistics_fc_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div.px-10.sticky.top-16.flex.flex-col.items-start.pt-4.bg-\[--netural-gray-scale-white\].z-10 > ul > li:nth-child(3) > button"
statistics_fc_add_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > main > div.px-10.flex.flex-col.gap-5 > div > div:nth-child(1) > ul > li:nth-child(1)"
statistics_fc_re_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > main > div.px-10.flex.flex-col.gap-5 > div > div:nth-child(1) > ul > li:nth-child(2)"
statistics_fc_expiration_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > main > div.px-10.flex.flex-col.gap-5 > div > div:nth-child(1) > ul > li:nth-child(3)"
statistics_pt_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div.px-10.sticky.top-16.flex.flex-col.items-start.pt-4.bg-\[--netural-gray-scale-white\].z-10 > ul > li:nth-child(4) > button"
statistics_pt_add_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > main > div.px-10.flex.flex-col.gap-5 > div.w-full.flex.flex-col.gap-5.mt-3 > div.flex > ul > li:nth-child(1) > button"
statistics_pt_re_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > main > div.px-10.flex.flex-col.gap-5 > div.w-full.flex.flex-col.gap-5.mt-3 > div.flex > ul > li:nth-child(2) > button"
statistics_pt_expiration_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > div > main > main > div.px-10.flex.flex-col.gap-5 > div.w-full.flex.flex-col.gap-5.mt-3 > div.flex > ul > li:nth-child(3) > button"
statistics_expiring_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div.px-10.sticky.top-16.flex.flex-col.items-start.pt-4.bg-\[--netural-gray-scale-white\].z-10 > ul > li:nth-child(5) > button" #실서버 전용 3-> 5
statistics_retained_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div.px-10.sticky.top-16.flex.flex-col.items-start.pt-4.bg-\[--netural-gray-scale-white\].z-10 > ul > li:nth-child(6) > button"
statistics_counsellor_selector = "body > div.relative.flex-1.flex.bg-\[--netural-gray-scale-white\] > div > main > div.px-10.sticky.top-16.flex.flex-col.items-start.pt-4.bg-\[--netural-gray-scale-white\].z-10 > ul > li:nth-child(7) > button" #실서버 전용 4 -> 7

#통계 관리 동작
def statistics_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #통계 관리 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_selector))
        )
        statistics = driver.find_element(By. CSS_SELECTOR, statistics_selector)
        statistics.click()
        print("통계 관리 선택 완료")
        
        #통계 관리 선택 후 딜레이 2초
        time.sleep(2)

        #결제 내역 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_payment_selector))
        )
        statistics_payment = driver.find_element(By. CSS_SELECTOR, statistics_payment_selector)
        statistics_payment.click()
        print("결제 내역 탭 선택 완료")

        #결제 내역 탭 선택 후 딜레이 2초
        time.sleep(2)

        # #회원권 탭 선택
        # wait_count += 1
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_fc_selector))
        # )
        # statistics_fc = driver.find_element(By. CSS_SELECTOR, statistics_fc_selector)
        # statistics_fc.click()
        # print("회원권 탭 선택 완료")

        # #회원권 탭 선택 후 딜레이 2초
        # time.sleep(1)

        # #회원권_재등록 탭 선택
        # wait_count += 1
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_fc_re_selector))
        # )
        # statistics_fc_re = driver.find_element(By. CSS_SELECTOR, statistics_fc_re_selector)
        # statistics_fc_re.click()
        # print("회원권 _ 재등록 탭 선택 완료")

        # #회원권 _ 재등록 탭 선택 후 딜레이 2초
        # time.sleep(1)

        # #회원권_만기 전 재등록 탭 선택
        # wait_count += 1
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_fc_expiration_selector))
        # )
        # statistics_fc_expiration = driver.find_element(By. CSS_SELECTOR, statistics_fc_expiration_selector)
        # statistics_fc_expiration.click()
        # print("회원권 _ 만기 전 재등록 탭 선택 완료")

        # #회원권 _ 만기 전 재등록 탭 선택 후 딜레이 2초
        # time.sleep(1)

        # #회원권_신규 등록 탭 선택
        # wait_count += 1
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_fc_add_selector))
        # )
        # statistics_fc_add = driver.find_element(By. CSS_SELECTOR, statistics_fc_add_selector)
        # statistics_fc_add.click()
        # print("회원권 _ 신규 등록 탭 선택 완료")

        # #회원권 _ 신규 등록 탭 선택 후 딜레이 2초
        # time.sleep(1)

        # #개인 레슨 탭 선택
        # wait_count += 1
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_pt_selector))
        # )
        # statistics_pt = driver.find_element(By. CSS_SELECTOR, statistics_pt_selector)
        # statistics_pt.click()
        # print("개인 레슨 탭 선택 완료")
        
        # #개인 레슨 탭 선택 후 딜레이 2초
        # time.sleep(1)

        # #개인 레슨 _ 재등록 탭 선택
        # wait_count += 1
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_pt_re_selector))
        # )
        # statistics_pt_re = driver.find_element(By. CSS_SELECTOR, statistics_pt_re_selector)
        # statistics_pt_re.click()
        # print("재등록 탭 선택 완료")

        # #재등록 탭 선택 후 딜레이 2초
        # time.sleep(1)

        # #개인 레슨 _ 만기 전 재등록 탭 선택
        # wait_count += 1
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_pt_expiration_selector))
        # )
        # statistics_pt_expiration = driver.find_element(By. CSS_SELECTOR, statistics_pt_expiration_selector)
        # statistics_pt_expiration.click()
        # print("만기 전 재등록 탭 선택 완료")

        # #만기 전 재등록 탭 선택 후 딜레이 2초
        # time.sleep(1)

        # #개인 레슨 _ 신규 등록 탭 선택
        # wait_count += 1
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_pt_add_selector))
        # )
        # statistics_pt_add = driver.find_element(By. CSS_SELECTOR, statistics_pt_add_selector)
        # statistics_pt_add.click()
        # print("신규 등록 탭 선택 완료")

        # #신규 등록 탭 선택 후 딜레이 2초
        # time.sleep(1)


        #만기 예정 회원 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_expiring_selector))
        )
        statistics_expiring = driver.find_element(By. CSS_SELECTOR, statistics_expiring_selector)
        statistics_expiring.click()
        print("만기 예정 회원 탭 선택 완료")

        #만기 예정 회원 탭 선택 후 딜레이 2초
        time.sleep(5)

        # #보유 회원 탭 선택
        # wait_count += 1
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_retained_selector))
        # )
        # statistics_retained = driver.find_element(By. CSS_SELECTOR, statistics_retained_selector)
        # statistics_retained.click()
        # print("보유 회원 탭 선택 완료")

        # #보유 회원 탭 선택 후 딜레이 2초
        # time.sleep(1)

        #상담자 탭 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, statistics_counsellor_selector))
        )
        statistics_counsellor = driver.find_element(By. CSS_SELECTOR, statistics_counsellor_selector)
        statistics_counsellor.click()
        print("상담자 탭 선택 완료")

        #상담자 탭 선택 후 딜레이 2초
        time.sleep(2)

    except (NoSuchElementException, TimeoutException):
         print("!!!!! 통계 관리 관련 오류 발생 !!!!!")

 
statistics_admin()
time.sleep(1)

#대시 보드 동작
dashboard_selector = "body > div.relative.flex.bg-\[--netural-gray-scale-white\] > nav > a"

def dashboard_admin():
    global wait_count # 글로벌 변수 선언
    try:
        #대시보드 선택
        wait_count += 1
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By. CSS_SELECTOR, dashboard_selector))
        )
        dashboard = driver.find_element(By. CSS_SELECTOR, dashboard_selector)
        dashboard.click()
        print("대시보드 선택 완료")
        time.sleep(1)

    except (NoSuchElementException, TimeoutException):
        print("!!!!! 대시보드 관련 오류 발생 !!!!!")

dashboard_admin()
time.sleep(1)


# 작업 끝난 후 호출 횟수 출력
print(f"{wait_count}개 항목 검증 완료")
print("5초 후 종료됩니다.")

# 카운트다운 출력
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# 드라이버 종료
driver.quit()