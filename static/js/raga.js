var svm_graphs = document.getElementById('svm');
var rfc_graphs = document.getElementById('rfc');
var knn_graphs = document.getElementById('knn');
var hom = document.getElementById('home');
var visual_graphs = document.getElementById('visual');
var password_page = document.getElementById('password_page');


function svm(){
svm_graphs.style.display='block';
rfc_graphs.style.display='none';
knn_graphs.style.display='none';
visual_graphs.style.display='none';
password_page.style.display='none';
hom.style.display='none';
}

function rfc(){
svm_graphs.style.display='none';
rfc_graphs.style.display='block';
knn_graphs.style.display='none';
visual_graphs.style.display='none';
password_page.style.display='none';
hom.style.display='none';
}

function knn(){
svm_graphs.style.display='none';
rfc_graphs.style.display='none';
knn_graphs.style.display='block';
visual_graphs.style.display='none';
password_page.style.display='none';
hom.style.display='none';
}

function home(){
svm_graphs.style.display='none';
rfc_graphs.style.display='none';
knn_graphs.style.display='none';
visual_graphs.style.display='none';
password_page.style.display='none';
hom.style.display='block';
}

function visual(){
svm_graphs.style.display='none';
rfc_graphs.style.display='none';
knn_graphs.style.display='none';
visual_graphs.style.display='block';
password_page.style.display='none';
hom.style.display='none';
}


function password(){
svm_graphs.style.display='none';
rfc_graphs.style.display='none';
knn_graphs.style.display='none';
visual_graphs.style.display='none';
password_page.style.display='block';
hom.style.display='none';
}