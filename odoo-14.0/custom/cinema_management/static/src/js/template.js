odoo.define("cinema_management.SampleTemplate", function (require){
   "use strict";

   var Screens = require("web.datepicker");
   console.log(Screens)
   var core = require('web.core');
   var _t = core._t;

   Screens.DateWidget.include({
        _onInputClicked: function () {
        this.__libInput++;
        this.$el.datetimepicker('toggle');
        this.__libInput--;
        this.focus();
        alert("Thank you for entering the date");
    }
   })
});