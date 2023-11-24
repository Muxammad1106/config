function showModal(modalId) {
    let modal = document.getElementById(modalId);
    modal.style.display = "block";
}

function closeModal(modalId) {
    let modal = document.getElementById(modalId);
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = "none";
    }
};
function loadAddLeadForm() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var modalContent = document.createElement('div');
            modalContent.innerHTML = this.responseText;
            showModal(modalContent);
        }
    };
    xhttp.open("GET", "add_lead.html", true);
    xhttp.send();
}

function showModal(content) {
    let modal = document.getElementById("addLeadModal");
    let modalContent = modal.querySelector(".modal-content");
    modalContent.innerHTML = "";
    modalContent.appendChild(content);
    modal.style.display = "block";
}

// Остальной код для модальных окон и функций закрытия