<script>
	import { WEBUI_BASE_URL } from '$lib/constants';
</script>

<div class="w-full h-screen max-h-[100dvh] text-white relative">
	<div class="w-full h-full absolute top-0 left-0 bg-white dark:bg-black"></div>

	<div class="w-full absolute top-0 left-0 right-0 h-8 drag-region" />

		<div class="fixed m-10 z-50">
			<div class="flex space-x-2">
				<div class=" self-center">
					<img
						id="logo"
						crossorigin="anonymous"
						src="{WEBUI_BASE_URL}/static/splash.png"
						class=" w-6 rounded-full"
						alt="logo"
					/>
				</div>
			</div>
		</div>
</div>
