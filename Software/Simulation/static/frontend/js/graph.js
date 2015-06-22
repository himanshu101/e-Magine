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
var G = ( function( G, d3 ){
	/**
	 * Function to extend functionality of parent in child
	 * @param  {Object} child  child object
	 * @param  {Object} parent parent object
	 * @return {null}
	 */
	G.extend = function ( child, parent ) {
		var copyOfParent = Object.create( parent.prototype );
		copyOfParent.constructor = child;
		child.prototype = copyOfParent;
	};
	/**
	 * constructor for graph object
	 * @param {[type]}
	 * @param {[type]}
	 */
	G.Graph = function( nodes, edges, type ) {
		this.nodes = nodes;
		this.edges = edges;
		this.nodes.forEach( function( node ) {
			node.adj = [];
			node.visited = 0;
		} );
		this.animation = new G.Animation();
		// 1 for directed or else undirected
		this.type = typeof type !== 'undefined' ? type : 0;
		this.force = null;
		this.svg = null;
	};
	G.Graph.prototype = {
		constructor: G.Graph,
		/**
		 * Generates adjacency list from a set of edges
		 * @return {null}
		 */
		generateAdjacency: function() {
			for ( var edge in this.edges ) {
				var link = this.edges[edge];
				//console.log(link);
				//console.log(link.source);
				link.source.adj.push( [link.target,link.w] );
				if ( this.type === 0 ) {
					link.target.adj.push( [link.source,link.w] );
				}
			}
		},
		/**
		 * Sorts the edges on the basis of edge weights
		 * @return {null}
		 */
		sortEdges: function() {
			var l = this.edges.length;
			for(var i=0;i<l-1;i++){
				var edge = this.edges[i];
				var pos=i;var tmp=null;var min=edge.w;
				for(var j=i+1;j<l;j++){
					var edgej=this.edges[j];
					if(min>edgej.w){
						pos=j;
						min=edgej.w;
						//console.log(nodej.d+" "+node.d);
					}
				}
				tmp = this.edges[i];
				this.edges[i] = this.edges[pos];
				this.edges[pos] = tmp;
			}
		},
		/**
		 * Gets the edge corresponding to source and destination vertex
		 * @return {object} edge
		 */
		getEdge: function( src, dest ) {
			var edge = null;
			for( var e in this.edges ) {
				var ed = this.edges[e];
				if( ed.source == src && ed.target == dest) {
					edge = ed;
					break;
				}
			}
			return edge;
		},
		/**
		 * Adds a new node
		 * @return {null}
		 */
		addNode: function( v ) {
			this.nodes.push( v );
		},
		/**
		 * Adds a new edge
		 * @return {null}
		 */
		addEdge: function( src, dest ) {
			var edge = {"source": src, "target": dest};
			src.adj.push( dest );
			if ( this.type === 0 ) {
				dest.adj.push( src );
			}
			this.edges.push( edge );
		},
		/**
		 * Initialize the graph with d3 rendering
		 * @param  {int} height height of canvas
		 * @param  {int} width  width of canvas
		 * @return {null}
		 */
		initialize: function ( height, width ) {
			// Scaling not done yet, values hardcoded
			this.svg = d3.select( 'body' ).append( 'svg' )
			.attr( 'width', width )
			.attr( 'height', height );
			this.force = d3.layout.force()
			.size([width, height])
			.linkDistance(210)
			.charge(-350)
			.nodes(this.nodes).links(this.edges);

			var link = this.svg.selectAll('.link')
						.data(g.edges)
						.enter()
						.append('g')
						.attr('class','link');
			var path = link.append( 'path' )
						.attr({
							'd': function(d) {return 'M '+d.source.x+' '+d.source.y+' L '+ d.target.x +' '+d.target.y},
							'class':'edgepath',
							'fill-opacity':1,
							'stroke-opacity':1,
							'stroke':'red',
							'marker-end': 'url(#end)',
							'id':function(d,i) {return 'edgepath'+i}
						});

			var node = this.svg.selectAll('.node')
						.data(this.nodes)
						.enter().append('svg')
						.attr('class','node');

			node.append("circle")
			.attr("r", width/30)
			.style("fill", function (d) {
				return d.color;
			});//add scaling here

			node.append("text")
				.attr("dx", -3)
				.attr("dy", ".35em")
				.text(function( d ) { return d.data !== 'undefined'?d.data:"1"; })
				.style("stroke", "orange");

			this.force.on( 'end', function() {
				d3.selectAll("circle").attr("r",width/30).attr("cx", function (d) {
					return d.x;
				})
				.attr("cy", function ( d ) {
					return d.y;
				});
				link.selectAll( 'path' ).attr( 'd', function( d ){
					return 'M '+d.source.x+' '+d.source.y+' L '+ d.target.x +' '+d.target.y;
				})
				.attr( 'marker-end', 'url(#end)' );
			});

			this.force.on( 'tick', function() {
				link.selectAll( 'path' ).attr( 'd',function( d ) {
					return 'M '+d.source.x+' '+d.source.y+' L '+ d.target.x +' '+d.target.y
				} )
				.attr('marker-end', 'url(#end)');
				d3.selectAll("circle").attr("r",width/30).attr("cx", function (d) {
					return d.x;
				})
				.attr("cy", function ( d ) {
					return d.y;
				});
			} );
			this.start();
		},
		/**
		 * Starts animation
		 * @return {null}
		 */
		start: function () {
			this.force.start();
		}
	};
	G.BFS = function( nodes, edges, type ) {
		G.Graph.call( this, nodes, edges, type );
		G.extend( G.BFS, G.Graph );
		this.color = ["blue","red","black"];//customization
	};

	/*G.BFS.prototype = {
		constructor: G.BFS,
		update: function () {
			var node = this.svg.selectAll('.node')
						.data(g.nodes);
			var nodes = node.selectAll("circle")
						.style("fill", function(d) { return d.color; });
			var link = svg.selectAll( '.link' );

		},
		algorithm: function( node ) {
			node.visited = 1;
			//animation is an array of objects
			//such an object consist of a node to change, and a set of properties changing
			this.animation.anim.push([{"node":node,val:"color","src":this.color[0],"dest":this.color[1]}]);
			var Q = [];
			Q.push(node);
			while( Q.length > 0 ) {
				var u = Q.pop();
				for( var i in u.adj ) {
					var v = u.adj[i];
					if( v.visited === 0 ) {
						this.animation.anim.push([{"node":v,val:"color","src":this.color[0],"dest":this.color[1]}]);
						Q.push(v);
						v.visited = 1;
					}
				}
				this.animation.anim.push([{"node":u,val:"color","src":this.color[1],"dest":this.color[2]}]);
			}
		}
	};*/
	return G;
}( G || {}, d3 ) );

