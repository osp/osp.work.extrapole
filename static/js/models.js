/*
 * 
 * models
 * 
 */


var app = app || {}


app.Message = Backbone.Model.extend({});

// window.bMa.Project = Backbone.Model.extend({
//     constructor: function() {
//         Backbone.Model.apply(this, arguments);
//         
//         var geo = this.get('geojson');
//         var ovl = new L.GeoJSON(geo, {
//             style:function(f){ 
//                 return bMa.Config().get_dict('/feature/style/show');
//             }
//         });
//         
//         this.set({display:true, feature:ovl});
//     },
//     bounds:function(){
//         if(this.layer === undefined || this.data.geojson.coordinates.length === 0)
//         {
//             var llb = new L.LatLngBounds();
//             return llb;
//         }
//         return this.layer.getBounds();
//     },
//     
// })