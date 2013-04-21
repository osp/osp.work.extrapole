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
    selected : false,
    events:{
        'click .mail-title': 'toggle',
    },
    render: function() {
        var data = this.model.toJSON();
        template.render('message', this.$el, function(t){
            this.html(t(data));
        });
        return this;
    },
    toggle: function(evt){
        var body = this.$el.find('.message-body');
        if(this.selected)
        {
            body.hide();
        }
        else
        {
            body.show();
        }
        this.selected = !this.selected;
    }
});

app.AppView = Backbone.View.extend({
    el:'body',
    initialize: function() {
        this.$maildir = $('<div id="maildir" />');
        app.Messages = new app.MessageList();
        
//         this.listenTo(app.Messages, 'add', this.addOne);
        this.listenTo(app.Messages, 'reset', this.addAll);
        this.listenTo(app.Messages, 'all', this.render);
        
        app.Messages.fetch({reset: true});
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

});