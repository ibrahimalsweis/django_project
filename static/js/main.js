

let id_content_comment = document.getElementById("id_content_comment")
let btn_submit = document.getElementById("submit")
console.log(btn_submit);
btn_submit.onclick = function () {
    console.log(id_content_comment.value);
}