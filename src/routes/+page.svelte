<script>
    import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

    onMount(() => {
        goto('/bike-share-toronto/growth');
    });

</script>

Hello World!