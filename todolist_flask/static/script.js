function editfunc(task_id) {
    var message_text = document.getElementById("writing_space").value;
    if (message_text != '') {
        alert('Another task is being edited!');
    }
    else{
        window.location.href='/edit-button/'+task_id
    }
}

function delfunc(task_id) {
    var confirm_delete = confirm('Are you sure you want to delete?');
    if (confirm_delete){
        window.location.href='/delete-button/'+task_id
    }
}

function logOut() {
    var confirm_delete = confirm('Are you sure you want to Log out?');
    if (confirm_delete){
        window.location.href='/'
    }
}