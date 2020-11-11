# iu-lyrics-generator

아이유 노래 가사를 이용하여 랜덤 가사 생성

## 제작 목적

그냥 `konply` 라이브러리의 예제를 보다가 가수 아이유 노래들로 가사를 랜덤하게 생성하면 어떨까 생각이 들었다.

## 데이터셋

사용된 노래 가사는 다음과 같습니다.

총 14397자입니다.

```
./data/Havana.txt
./data/Into the island.txt
./data/Modern Times.txt
./data/Obliviate.txt
./data/Voice Mail.txt
./data/그렇게 사랑은.txt
./data/누구나 비밀은 있다.txt
./data/마침표.txt
./data/분홍신.txt
./data/블루밍.txt
./data/삐삐.txt
./data/싫은 날.txt
./data/에잇.txt
./data/우울시계.txt
./data/을의 연애.txt
./data/이런 엔딩.txt
./data/이름에게.txt
./data/이지금.txt
./data/입술 사이 (50cm).txt
./data/잼잼.txt
./data/좋은 날.txt
./data/팔레트.txt
./data/한낮의 꿈.txt
```

노래 가사는 저작권 문제로 따로 포함하진 않았습니다.

직접 돌려보고 싶으시다면 ./data/ 디랙토리에 가사 파일을 올려주세요.

## Result

### initstr `비밀`

```
 비밀 이란 없다고 Oh oh
 한번 도 겁 내지 마 사람 들 은 있는 거 알잖아 네 책임 도
 I feel blue
 다시
 Anything
 널 찾을까
 Repeat repeat
 두 입술 사이 거린 아직 까진 50 cm
 But right
 편하게 하지 마
 우울한 결말 따위 는 없어
 멀어져 가는
 주머니 속 은 또 다른 나 는 끝나지 않을 거야 Ooh Whatever
 그림자 없이
 덕분 에
 걷 잡 을 해
 그리움 과 걱정 사라지네 난 여행 해 얼굴 좀 해
 은근 한 별 것 도
 ```

### initstr `사랑`

```
 사랑 은 비슷하지만
 Whoa oh
 혼자 란 섬 에서
 그 메아리 만 끌어
 나쁜 기억 은 나 예요 놀랄 거 알 것 을
 친구 가 알 아 들어 ?
 이제 그만 할까 내 마음 아
 우리 의
 이런 나를 비추던 Summer Time
 한 걸음 도 녹을까 햇볕 드는 좋은 기억 을 나 혼자 란 섬
 언젠가 나도
 동네 몇 바퀴 를 보면서 웃어도
 oh , run for our lives
 덮고 그 말 틀려 ?
 누구 에게도 말 못 하게 입 에 다시 얹고 또다시
 우울하다
```

### initstr `우울`

```
 우울 시계 가 별로 였는지
 다시 만나
 물음표 없이 보낼게 사랑 은 꼭 그 사람 을 막고서 막 넘어가고 있네
 하긴 그래도 여전히
 Baby make me oh my business
 그 이유 를 나눠
 애
 제발 내 마음 아 Obliviate
 Repeat repeat
 어쩜 이렇게 하늘 은 마치 재난 문자 같지
 알 만 돌아와
 I feel blue blue
 엄지손가락 으로
 겨우 스무고개 넘어 기쁨 도 없는
 너무 비 좁아
 모두 안녕 모두 사라질 세상 만사 귀찮아
 난 하나 인 것 도
 시들지 않는 영원한 것
 ```

### initstr `너`

```
 너 를 내게 멈춰있길 바 둠 멈추지 말고 가 
 속 아주 깜깜 했지
 우우
 이런 나를 비추던 Summer Time 너 에게 한 사람 내 마음 인지
 보이지 않도록 멀어도
 우리
 그 목소리 가 되어
 이제 조금 은 뜨겁 기 는커녕 peacock Blue blue
 덮고 그 위 에
 머리 야 오 말 어쩌면 다신 못 하게 또 예요 놀랄 거 없이
 그렇게 아픈 거 알 아 들어
 우울하다
 가자 이 꺼진 것 같 애
 아파 얼마나 사랑 해줄 사람 어디 없나 비 나 의 아랫 입술
 We
 ```

## 마무리

이상하다
