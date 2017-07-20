

var credential = {
    "username": "ddasacas",
    "password": "dasddaaasa"
}
var profile = {
    "name": "郭嘉琦",
    "title": "研发工程师",
    "company": "杭州美登科技",
    "address": "西城纪",
    "birth": "1992-10-27",
    "email": "asdaw@qwqq.com",
    "phone": "13920285112"
}
var url = "http://127.0.0.1:9000/public_api/signup"
function onClick() {
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            "credential": JSON.stringify(credential),
            "profile": JSON.stringify(profile)
        }
    });
}