# issue

## 1. Django 3.0 Language_CODE

이전 2버전에서는 `ko-kr`을 사용하면 되었는데 똑같이 설정해주니 아래와 같이 오류가 발생했다.

```bash
ERRORS:
?: (translation.E004) You have provided a value for the LANGUAGE_CODE 
setting that is not in the LANGUAGES setting.
```

찾아보니 설정이 바뀌었다.

> 참고자료
>
>  https://github.com/django/django/blob/master/django/conf/global_settings.py

`ko`로 설정하면 한국어로 바뀐다.

