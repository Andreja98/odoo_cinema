odoo.define("cinema_management.SampleTemplate", function (require){
   "use strict";

   var Screens = require("web.datepicker");
   console.log(Screens)
   var core = require('web.core');
   var _t = core._t;

   Screens.DateWidget.include({
        _onDateTimePickerHide: function () {
        this.__isOpen = false;
        this.changeDatetime();
        if (this._onScroll) {
            window.removeEventListener('wheel', this._onScroll, true);
        }
        this.changeDatetime();
        alert("Thank you for entering the date")
    }
   })
});