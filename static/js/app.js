/*
 * 
 * app.js
 * 
 */

var app = app || {}

$(function() {
    
    // TODO
    $('body').append('<div id="about-box"><h1>Présentation</h1><p>Ici pourra venir se loger la présentation d’Extrapole.</p></div>');
    $('body').append('<div id="agenda-box"><h1>Agenda</h1><p>Et ici pourra venir se loger l’agenda.</p></div>');
    
    
    new app.AppView();
    
    
});