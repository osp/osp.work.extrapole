/*
 * 
 * collections
 * 
 */


var app = app || {}

app.MessageList = Backbone.Collection.extend({
    url:'/maildir/',
    model:app.Message,
});


