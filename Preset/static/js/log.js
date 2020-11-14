$(document).ready(function () {
    console.log('ready works');

    let valid_login = false;
    let valid_password = false;

    let loginExp = /^[a-zA-Z0-9][a-zA-Z0-9_]{4,14}$/
    let passExp = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{7,15}$/;
    $('#check').click(function () {
    $('#login_field').change(function () {
        let _login = $(this).val()
        // console.log(loginExp.test(_login))
        if (!loginExp.test(_login)){  // логин не валидный
            $('#login_ico').attr('src', '../../static/img/error.png')
            $('#login_err').text('Логин должен быть длинной 5-15 символов и состоять из букв и цифр!')
            valid_login = false;
        }else{// логин валидный

            $.ajax({
                url: '/ajax_reg_login',
                data: 'login_field=' + _login,
                success: function (result) {
                    if (result.message_login === 'занят'){
                        $('#login_ico').attr('src', '../../static/img/win.png')
                        $('#login_err').text('')
                        valid_login = true;
                    }else{
                        $('#login_ico').attr('src', '../../static/img/error.png')
                        $('#login_err').text('Такой логин не существует!!!!!!')
                        valid_login = false;
                    }
                }

            })


        }
    })

    $('#login_field').focus(function () {
        $('#login_ico').attr('src', '../../static/img/question.png')
        $('#login_err').text('')
    })
     $('#password_field').click(function () {
        let _pass1 = $(this).val()
        if (passExp.test(_pass1)){ // валидный емайл
            $('#password_ico').attr('src', '../../static/img/win.png')
            $('#password_err').text('')
            valid_password = true;
        }else{// не валидный емайл
            $('#password_ico').attr('src', '../../static/img/error.png')
            $('#password_err').text('Пароль должен содержать хотя-бы одну заглавную букву и цыфры, количество символов 8-16!!!')
            valid_password = false;
        }
    })

    $('#password_field').focus(function () {  // сброс ошибок и иконок
        $('#password_ico').attr('src', '../../static/img/question.png')
        $('#password_err').text('')
    })
    $('#submit').click(function () {
        if (
            valid_login === true &&
            valid_password === true


        ){
            $('.form-group').attr('onsubmit', 'return true')
        }

    })
})
})
