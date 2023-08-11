<script>
    import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

    onMount(() => {
        goto('/growth');
    });

</script>

Hello World!