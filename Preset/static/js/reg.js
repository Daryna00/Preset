$(document).ready(function () {
    console.log('ready works');

    let valid_login = false;
    let valid_email = false;
    let valid_password = false;
    let valid_password2 = false;

    let loginExp = /^[a-zA-Z0-9][a-zA-Z0-9_]{4,14}$/
    let regExp_email = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
    let passExp = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{7,15}$/;
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
                        $('#login_ico').attr('src', '../../static/img/error.png')
                        $('#login_err').text('Логин уже занят!!!!!!')
                        valid_login = false;
                    }else{
                        $('#login_ico').attr('src', '../../static/img/win.png')
                        $('#login_err').text('')
                        valid_login = true;
                    }
                }

            })


        }
    })

    $('#login_field').focus(function () {
        $('#login_ico').attr('src', '../../static/img/question.png')
        $('#login_err').text('')
    })



    $('#email_field').blur(function () {
        let _email = $(this).val()
        if (regExp_email.test(_email)){ // валидный емайл
            $('#email_ico').attr('src', '../../static/img/win.png')
            $('#email_err').text('')
            valid_email = true;
        }else{// не валидный емайл
            $('#email_ico').attr('src', '../../static/img/error.png')
            $('#email_err').text('Недопустимая почта!!!')
            valid_email = false;
        }
    })

    $('#email_field').focus(function () {  // сброс ошибок и иконок
        $('#email_ico').attr('src', '../../static/img/question.png')
        $('#email_err').text('')
    })


    $('#password_confirm_field').blur(function () {
        let _pass2 = $(this).val()
        if (passExp.test(_pass2)){ // валидный емайл

                 $.ajax({
                url: '/ajax_reg_pass2',
                data: 'password_confirm_field=' + _pass2,
                success: function (result) {
                    if (result.message_pass2 === 'совпадает'){
                        $('#password_confirm_ico').attr('src', '../../static/img/win.png')
                        $('#password_confirm_err').text('')

                        valid_password2 = true;
                    }else{
                        $('#password_confirm_ico').attr('src', '../../static/img/error.png')
                        $('#password_confirm_err').text('!!!!!!')
                        valid_password2 = false;
                    }
                }

            })

        }else{// не валидный емайл
            $('#password_confirm_ico').attr('src', '../../static/img/error.png')
            $('#password_confirm_err').text('Пароль должен содержать большие и маленькие буквы и цыфры, количество символов 8-16!!!')
            valid_password = false;
        }
    })

    $('#password_confirm_field').focus(function () {  // сброс ошибок и иконок
        $('#password_confirm_ico').attr('src', '../../static/img/question.png')
        $('#password_confirm_err').text('')
    })


    $('#password_field').blur(function () {
        let _pass1 = $(this).val()
        if (passExp.test(_pass1)){ // валидный емайл
            $('#password_ico').attr('src', '../../static/img/win.png')
            $('#password_err').text('')
            valid_password = true;
        }else{// не валидный емайл
            $('#password_ico').attr('src', '../../static/img/error.png')
            $('#password_err').text('Пароль должен содержать буквы и цыфры, количество символов 8-16!!!')
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
            valid_email === true &&
            valid_password2 === true &&
            valid_password === true
        ){
            $('.form-group').attr('onsubmit', 'return true')
        }
    })

})