/*
 * 
 * views
 * 
 */

var app = app || {}

app.MessageView = Backbone.View.extend({
//     initialize: function() {
//         Backbone.View.apply(this, arguments);
//         this.listenTo(this.model, 'change', this.render);
//     },
    render: function() {
        var data = this.model.toJSON();
        template.render('message', this.$el, function(t){
            this.html(t(data));
        });
        return this;
    },
});

app.AppView = Backbone.View.extend({
    el:'body',
    initialize: function() {
        this.$maildir = $('<div id="maildir" />');
        app.Messages = new app.MessageList();
        this.listenTo(app.Messages, 'add', this.addOne);
        this.listenTo(app.Messages, 'reset', this.addAll);
        
        // New
        this.listenTo(app.Messages, 'change:completed', this.filterOne);
        this.listenTo(app.Messages, 'filter', this.filterAll);
        this.listenTo(app.Messages, 'all', this.render);
        
        app.Messages.fetch();
    },
    render: function() {
        this.$el.append(this.$maildir);
        return this;
    },
    addOne: function( message ) {
        var view = new app.MessageView({ model: message });
        this.$maildir.append( view.render().el );
    },
    
    addAll: function() {
        this.$maildir.html('');
        app.Messages.each(this.addOne, this);
    },
    
    // New
    filterOne : function (message) {
        message.trigger('visible');
    },
    
    // New
    filterAll : function () {
        app.Messages.each(this.filterOne, this);
    },
});