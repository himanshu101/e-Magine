var LabeledCircle = fabric.util.createClass(fabric.Circle, {

        type: 'labeledCircle',

        initialize: function(options) {
            options || (options = { });

            this.callSuper('initialize', options);
            this.set('radius',24);
            this.set('label', options.label || '');
        },

      toObject: function() {
        return fabric.util.object.extend(this.callSuper('toObject'), {
          label: this.get('label')
        });
      },
    
      _render: function(ctx) {
        this.callSuper('_render', ctx);

        ctx.font = '15px Helvetica';
        ctx.fillStyle = '#333';
        ctx.fillText(this.label, -this.radius/2.5 , 1.5*this.radius  );
        }
});

var codeIsShowing=1;

function codeShow(){
                    if(codeIsShowing == 1){
                        codeIsShowing=0;
                        $('#codebtn').text("Show Code");
                        $(".code").hide();
                    }
                    else{
                        codeIsShowing=1;
                        $('#codebtn').text("Hide Code");
                        $(".code").show();
                    }
                }
function refresh(){
                    document.getElementById("inputstr").value="";
                }

function getRadioValue()
                {
                        for (var i = 0; i < document.getElementsByName('optradio').length; i++)
                    {
                        if (document.getElementsByName('optradio')[i].checked)
                        {
                            return i;
                        }
                    }
                }