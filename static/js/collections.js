/*
 * 
 * collections
 * 
 */


var app = app || {}

app.MessageList = Backbone.Collection.extend({
    url:'/maildir/',
    model:app.Message,
    comparator: function( msg ) {
        return msg.get('timestamp') * -1;
    }
});


