$(document).ready(function () {
    console.log('ready works');

    // $('#login_field').click(function () {
    //     alert("ВНИМАНИЕ!!! КЛИК ПО ЛОГИНУ!!!")
    // })
    let valid_login = false;
    let valid_email = false;

    let loginExp = /^[a-zA-Z0-9][a-zA-Z0-9_]{4,14}$/
    let regExp_email = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
    $('#login_field').change(function () {
        let _login = $(this).val()
        // console.log(loginExp.test(_login))
        if (!loginExp.test(_login)){  // логин не валидный
            $('#login_ico').attr('src', '../../static/img/error.png')
            $('#login_err').text('Логин должен быть длинной 5-15 символов и состоять из букв и цифр!')
            valid_login = false;
        }else{// логин валидный

            $.ajax({
                url: '/ajax_reg',
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

    $('#submit').click(function () {
        if (
            valid_login === true &&
            valid_email === true
        ){
            $('.form-group').attr('onsubmit', 'return true')
        }
    })

})