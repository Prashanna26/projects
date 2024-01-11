document.addEventListener("DOMContentLoaded", function () {
  getTasks()

  document.getElementById("myForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission
    const inputField = document.getElementById("writing_space")
    const datentime = document.getElementById("datentime")
    const date = datentime.value;
    const text_data = inputField.value;
    inputField.value = ''
    datentime.value = ''
    const data = {
      'message': text_data,
      'Date':date,
      'status': 0
    };

    fetch("/button-clicked", {
      method: "POST",
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    getTasks();
  })

  function getTasks(){
    fetch("/button-clicked", {
      headers: {
        'Content-type': 'application/json'
      },
    })
      .then(response => response.text())
      .then(data => {
        document.getElementById("output").innerHTML = data;

        const deleteButtons = document.querySelectorAll('.del_button');
        deleteButtons.forEach(button => {
        button.addEventListener('click', onClickDeleteBtn);
        })

        const completeButtons = document.querySelectorAll('.com_button');
        completeButtons.forEach(button => {
        button.addEventListener('click', onClickCompleteBtn);
        })

        const editButtons = document.querySelectorAll('.edit_button');
        editButtons.forEach(button => {
        button.addEventListener('click', onClickEditBtn);
        })

      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  function onClickDeleteBtn(event) {
    const button_index_id = event.currentTarget.dataset.deleteId;

    id_value = {
      'message': button_index_id
    }
    fetch("/delete-button", {
      method: "POST",
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(id_value)
    })
    .then(response => {
      response.text();
      if (response.ok){
        getTasks();
      }
    })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  function onClickCompleteBtn(event) {
    const status_index_id = event.currentTarget.dataset.statusId;
    id_status = {
      'message': status_index_id
    }
    fetch("/complete-button", {
      method: "POST",
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(id_status)
    })
    .then(response => {
      response.text();
      if (response.ok){
        getTasks();
      }
    })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  function onClickEditBtn(event) {
    const edit_index_id = event.currentTarget.dataset.editId;
    const message_text = document.getElementById("writing_space")



    id_edit = {
      'message': edit_index_id
    }
    fetch("/edit-button", {
      method: "POST",
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(id_edit)
    })

    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not OK');
      }
      return response.text();
    })
    .then(data => {
      const dataArray = data.split(',')
      document.getElementById("writing_space").value = dataArray[0]
      document.getElementById("datentime").value =dataArray[1].trim()
      getTasks();
    })
    .catch(error => {
      console.error('Error:', error);
    });
  
  }
})  


