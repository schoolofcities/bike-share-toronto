 <script>
        import { getContext, createEventDispatcher } from "svelte";

        const { data, xGet, yGet, xScale, yScale } = getContext('LayerCake');

        export let fill;
        let hideTooltip = false;
      
        const dispatch = createEventDispatcher();
        
        function handleMousemove(feature) {
          return function handleMousemoveFn(e) {
            raise(this);
            // When the element gets raised, it flashes 0,0 for a second so skip that
            if (e.layerX !== 0 && e.layerY !== 0) {
              dispatch("mousemove", { e });
            }
          };
        }

    </script>
      <g
      class="bar-group"
      on:mouseout={(e) => dispatch("mouseout")}
      on:blur={(e) => dispatch("mouseout")}
      >
        {#each $data as d, i}
          <rect
            class='group-rect'
            data-id="{i}"
            x="{$xScale.range()[0]}"
            y="{$yGet(d)}"
            height={$yScale.bandwidth()}
            width="{$xGet(d)}"
            {fill}              
            on:mouseover={(e) => dispatch("mousemove", { e, props: d })}
            on:focus={(e) => dispatch("mousemove", { e, props: d })}
            on:mousemove={(e) => handleMousemove(e, d)}
          ></rect>


        {/each}
      </g>