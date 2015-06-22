/**
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
* See the GNU General Public License for more details.
* You should have received a copy of the GNU General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
var G = ( function( G, d3){
	/**
	 * Constructor to define the animation obejct
	 * Each animation object consists of an array of changing values
	 * Each changing value consists of a source value and a destination value
	 */
	G.Animation = function() {
		this.anim = [];
		this.index = 0;
		this.timer = null;
	};
	G.Animation.prototype = {
		constructor: G.Animation,
		/**
		 * Execute the next step of animation
		 * by changing the properties and calling the update method
		 * @param  {function} updater - updating function
		 * @param  {array} args - array of parameters
		 * @return {null}
		 */
		next: function( updater, args ) {
			if ( this.index < this.anim.length ) {
				this.evaluate( 0 );
				this.index++;
				updater.apply( null, args );
			} else {
				console.log( "Animation over" );
				this.stopAnimation();
			}
		},
		/**
		 * Execute the previous step of animation
		 * by changing the properties and calling the update method
		 * @param  {function} updater - updating function
		 * @param  {array} args - array of parameters
		 * @return {null}
		 */
		prev: function( updater, args ) {
			if ( this.index >= 0 ) {
				this.index--;
				this.evaluate( 1 );
				updater.apply( null, args );
			} else {
				console.log( "Animation over" );
				$('.status span').text( "Animation over" );
			}
		},
		/**
		 * Evaluate the animation at this particular moment
		 * @param  {integer} dir - direction of animation
		 * @return {null}
		 */
		evaluate: function( dir ) {
			var state = this.anim[ this.index ];
			for ( var i in state ) {
				var item = state[i];
				if ( dir === 0 ) {
					item.node[item.val] = item.dest;
					//console.log(item);
				} else {
					item.node[item.val] = item.src;
				}
			}
		},
		/**
		 * Function to start automatic animation
		 * @param  {integer} interval - duration of intervals of animation
		 * @return {null}
		 */
		startAnimation: function( updater, interval ) {
			if ( this.timer === null ) {
				var self = this;
				this.timer = setInterval( function(){
					self.next( updater );
				}, interval );
			} else {
				console.log( "one animation already in progress" );
				console.log(this.timer);
				$('.status span').text( "one animation already in progress" );
			}
		},
		stopAnimation: function() {
			if ( this.timer !== null ) {
				clearInterval(this.timer);
				this.timer = null;
			}
		},
		resetAnimation: function() {
			this.anim = [];
			this.index = 0;
			this.timer = null;
		}
	};
	return G;
}( G || {}, d3 ) );
