![image](https://github.com/user-attachments/assets/446da286-d2ae-4840-ad7d-1cfcd042b9f4)

![image](https://github.com/user-attachments/assets/81357d72-028e-4f23-b621-7f317ecc4e64)

![image](https://github.com/user-attachments/assets/0496fc62-7dee-4ad5-a1a6-b5f2ab93b9ba)

![image](https://github.com/user-attachments/assets/89728f9e-b166-46b3-8234-bc7c5bccb3d8)

# On Fit: 동국대학교 구성원을 위한 날씨 맞춤형 의상 추천 서비스

**On Fit**은 동국대학교 구성원들을 대상으로, 현재 날씨와 개인의 컨디션을 고려하여 최적의 의상을 추천해주는 서비스입니다. 사용자는 간단한 설정을 통해 개인화된 의상 추천을 받을 수 있으며, 피드백을 통해 추천 정확도를 지속적으로 향상시킬 수 있습니다.

## 주요 기능

1. **회원가입 및 로그인**
   - 사용자는 계정을 생성하고 로그인하여 개인화된 서비스를 이용할 수 있습니다.

2. **유저 초기 설정**
   - **위치 설정**: 기본 위치는 동국대학교로 설정되며, 사용자가 직접 위치를 설정할 수 있습니다.
   - **옷 선호도 설정**: 선호하지 않는 의상을 설정하여 추천 목록에서 제외할 수 있습니다.

3. **오늘의 옷 추천 단계**
   - **사용자 컨디션 및 활동성 입력**: 사용자는 현재 컨디션(예: 감기)과 활동 장소(실내 또는 실외)를 입력합니다. 이 정보는 의상 추천 시 가중치로 반영됩니다.
   - **날씨 정보 불러오기**: 현재 위치의 실시간 날씨 정보를 가져옵니다.
   - **의상 추천 결정**:
     - 기본 온도에 따른 레벨 설정에 사용자 입력 정보를 반영하여 최종 레벨을 결정합니다.
     - 아우터, 상의, 하의, 액세서리 등 카테고리별로 의상을 추천합니다.
     - 일교차가 10도 이상일 경우, "일교차가 큽니다. 겉옷을 챙기세요."와 같은 안내 문구를 제공합니다.
     - [사진 기능 구현 시] 동일한 레벨에서 과거에 입었던 의상 사진을 불러와 참고할 수 있습니다.

4. **유저 피드백 단계**
   - **가중치 조정**: 사용자는 추천된 의상에 대한 피드백을 제공하여 추천 알고리즘의 정확도를 높일 수 있습니다.
   - **사진 업로드**: [사진 기능 구현 시] 사용자는 자신의 의상 사진을 업로드하여 기록하고 공유할 수 있습니다.

5. **로그아웃**
   - 사용자는 언제든지 계정에서 로그아웃할 수 있습니다.

**On Fit**은 동국대학교 구성원들의 일상적인 의상 선택에 도움을 주기 위해 개발된 서비스로, 개인의 선호도와 실시간 날씨 정보를 반영하여 최적의 의상을 추천합니다. 

--- 
#python manage.py shell 입력 후, outfit 분류 데이터값 저장

from weather.models import Outfit

# Level 1: 매우 더운 날씨 (30°C 이상)
Outfit.objects.create(name="반팔 티셔츠", category="top", warmth_level=1, is_frequent=True)
Outfit.objects.create(name="민소매 티셔츠", category="top", warmth_level=1, is_frequent=True)
Outfit.objects.create(name="얇은 린넨 셔츠", category="top", warmth_level=1, is_frequent=True)
Outfit.objects.create(name="반바지", category="bottom", warmth_level=1, is_frequent=True)
Outfit.objects.create(name="린넨 바지", category="bottom", warmth_level=1, is_frequent=True)
Outfit.objects.create(name="슬랙스 (얇은 소재)", category="bottom", warmth_level=1, is_frequent=True)
Outfit.objects.create(name="양산", category="other", warmth_level=1, is_frequent=True)
Outfit.objects.create(name="선글라스", category="other", warmth_level=1, is_frequent=True)

# Level 2: 더운 날씨 (23°C ~ 29°C)
Outfit.objects.create(name="가벼운 자켓 (바람막이)", category="outer", warmth_level=2, is_frequent=True)
Outfit.objects.create(name="얇은 긴팔 티셔츠 (면 소재)", category="top", warmth_level=2, is_frequent=True)
Outfit.objects.create(name="가벼운 셔츠", category="top", warmth_level=2, is_frequent=True)
Outfit.objects.create(name="얇은 맨투맨 (아침저녁 대비용)", category="top", warmth_level=2, is_frequent=True)
Outfit.objects.create(name="반바지", category="bottom", warmth_level=2, is_frequent=True)
Outfit.objects.create(name="청바지 (얇은 소재)", category="bottom", warmth_level=2, is_frequent=True)
Outfit.objects.create(name="슬랙스 (면 소재)", category="bottom", warmth_level=2, is_frequent=True)
Outfit.objects.create(name="얇은 스카프 (바람 차단용)", category="other", warmth_level=2, is_frequent=True)

# Level 3: 선선한 날씨 (15°C ~ 22°C)
Outfit.objects.create(name="가디건", category="outer", warmth_level=3, is_frequent=True)
Outfit.objects.create(name="얇은 자켓", category="outer", warmth_level=3, is_frequent=True)
Outfit.objects.create(name="트렌치코트", category="outer", warmth_level=3, is_frequent=True)
Outfit.objects.create(name="니트", category="top", warmth_level=3, is_frequent=True)
Outfit.objects.create(name="스웨터", category="top", warmth_level=3, is_frequent=True)
Outfit.objects.create(name="긴팔 셔츠", category="top", warmth_level=3, is_frequent=True)
Outfit.objects.create(name="청바지", category="bottom", warmth_level=3, is_frequent=True)
Outfit.objects.create(name="슬랙스", category="bottom", warmth_level=3, is_frequent=True)
Outfit.objects.create(name="면바지", category="bottom", warmth_level=3, is_frequent=True)
Outfit.objects.create(name="얇은 목도리 (밤에 대비)", category="other", warmth_level=3, is_frequent=True)

# Level 4: 쌀쌀한 날씨 (5°C ~ 14°C)
Outfit.objects.create(name="울코트", category="outer", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="두꺼운 가디건", category="outer", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="두꺼운 트렌치코트", category="outer", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="경량 패딩", category="outer", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="기모 맨투맨", category="top", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="두꺼운 니트", category="top", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="기모 후드티", category="top", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="기모 청바지", category="bottom", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="기모 슬랙스", category="bottom", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="조거팬츠", category="bottom", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="기모 장갑", category="other", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="머플러", category="other", warmth_level=4, is_frequent=True)
Outfit.objects.create(name="귀마개 (추운 날 대비)", category="other", warmth_level=4, is_frequent=True)

# Level 5: 매우 추운 날씨 (5°C 이하)
Outfit.objects.create(name="롱패딩", category="outer", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="숏패딩 (두꺼운 종류)", category="outer", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="무스탕", category="outer", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="두꺼운 울코트", category="outer", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="기모 터틀넥", category="top", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="히트텍 상의 (발열 내의)", category="top", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="두꺼운 스웨터", category="top", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="기모 바지", category="bottom", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="레깅스 (보온용 레이어드)", category="bottom", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="기모 스웨트팬츠", category="bottom", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="방한 장갑", category="other", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="목도리 (캐시미어 등 따뜻한 소재)", category="other", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="털모자", category="other", warmth_level=5, is_frequent=True)
Outfit.objects.create(name="방한 귀마개", category="other", warmth_level=5, is_frequent=True)
