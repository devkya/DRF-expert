# FrontEnd
1. vue cli 사용하여 UI 설계
2. Handle anchors with Vue Router [링크](https://stackoverflow.com/questions/45201014/how-to-handle-anchors-bookmarks-with-vue-router)
3. Multi page & Router

## 해결해야 되는 것
1. `v-menu` width 더 크게 -> `v-navigation-bar` 로 해결
2. hash & ancher -> scroll 이동
3. `app-bar` 에서 메뉴를 클릭하면 `router-view`로 데이터가 전달되고, `HomeView.vue`에서 이벤트가 실행되어야 함
4. pagination 기능 추가 => drf 기능으로 해결되는 것 같음 => 강의 들으면서 해결

# DRF
## APIView, Mixins, Generics API View, ViewSet  
> [참고링크](https://velog.io/@duo22088/DRF-APIView-Mixins-generics-APIView-ViewSet-%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C)  
>`APIView` < `Mixins` < `generics APIView` < `ViewSet`
* `APIView`
    * 하나의 CBV 이므로 하나의 URL 만 처리 가능
    * 각 요청 method(get, post, put, delete)에 맞게 멤버함수를 구현하면, 해당 method 요청이 들어올 때 호출됨
    * 호출이 되면 호출 이전 단계(initial)에서 다음을 처리함
        1. 직렬화
        2. 인증 체크
        3. 사용량 제한 체크
        4. 권한 클래스 지정 : 비인증 / 인증 유저에 대한 API 호출
        5. 요청한 버전 체크 : request.version에 저장

* `Mixins`
    * `APIView` 구현에서 각 request method 마다 직접 직렬화 처리를 반복함 => `Mixins`를 사용하여 간소화 가능
    *  `queryset`과 `serializer_class`를 지정해주고 상속받은 `Mixins`와 연결해주면 됨
    * request method 와 연결되는 부분은 Customizing 해야 함

* `generics APIView`
    * 하나 이상의 `Mixins`와 결합된 클래스 제공

* `ViewSet`
    * 하나의 핼퍼클래스로 두 개 이상의 URL 처리 가능


## ViewSet vs Generic Views
### Generic Views
1. data from db
2. serialize
3. response
>listAPIView => `many=True` instance를 여러개 serialize 함
>RetrieveAPIView => `many=False` instance를 한 개만 serialize 함