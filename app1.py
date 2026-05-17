<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rakesh | DevOps Engineer</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
  <style>
    body {
      font-family: 'Inter', system-ui, sans-serif;
    }
    .hero-bg {
      background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.8)), 
                  url('https://source.unsplash.com/random/1920x1080/?cloud-infrastructure') center/cover no-repeat;
    }
    .card-hover {
      transition: all 0.3s ease;
    }
    .card-hover:hover {
      transform: translateY(-10px);
      box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
    }
  </style>
</head>
<body class="bg-gray-950 text-gray-100">

  <!-- Navbar -->
  <nav class="fixed top-0 w-full bg-gray-950 border-b border-gray-800 z-50">
    <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
      <div class="text-2xl font-bold text-emerald-400">RAKESH</div>
      <div class="hidden md:flex space-x-8">
        <a href="#about" class="hover:text-emerald-400 transition">About</a>
        <a href="#skills" class="hover:text-emerald-400 transition">Skills</a>
        <a href="#projects" class="hover:text-emerald-400 transition">Projects</a>
        <a href="#contact" class="hover:text-emerald-400 transition">Contact</a>
      </div>
      <a href="#" class="bg-emerald-600 hover:bg-emerald-500 px-5 py-2 rounded-lg font-medium transition">
        Download Resume
      </a>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="hero-bg h-screen flex items-center">
    <div class="max-w-6xl mx-auto px-6 text-center">
      <h1 class="text-6xl md:text-7xl font-bold mb-4">
        Hi, I'm <span class="text-emerald-400">Rakesh</span>
      </h1>
      <p class="text-3xl md:text-4xl text-gray-300 mb-6">DevOps & Cloud Engineer</p>
      <p class="text-xl text-gray-400 max-w-2xl mx-auto mb-10">
        Building scalable infrastructure, automating deployments, and delivering reliable systems.
      </p>
      <div class="flex justify-center gap-6">
        <a href="#projects" 
           class="bg-emerald-600 hover:bg-emerald-500 px-8 py-4 rounded-xl font-semibold text-lg transition">
          View My Work
        </a>
        <a href="#contact" 
           class="border border-gray-400 hover:border-white px-8 py-4 rounded-xl font-semibold text-lg transition">
          Get In Touch
        </a>
      </div>
      <div class="mt-16 flex justify-center gap-8 text-3xl">
        <a href="#" class="hover:text-emerald-400 transition"><i class="fab fa-linkedin"></i></a>
        <a href="#" class="hover:text-emerald-400 transition"><i class="fab fa-github"></i></a>
        <a href="#" class="hover:text-emerald-400 transition"><i class="fab fa-twitter"></i></a>
      </div>
    </div>
  </section>

  <!-- About -->
  <section id="about" class="py-20 bg-gray-900">
    <div class="max-w-6xl mx-auto px-6">
      <h2 class="text-4xl font-bold text-center mb-12">About Me</h2>
      <div class="grid md:grid-cols-2 gap-12 items-center">
        <div>
          <img src="https://source.unsplash.com/random/600x600/?indian-man" 
               alt="Rakesh" 
               class="rounded-2xl w-full shadow-2xl">
        </div>
        <div class="space-y-6">
          <p class="text-lg text-gray-300">
            Passionate DevOps Engineer with 4+ years of experience in designing, implementing, and maintaining 
            CI/CD pipelines, cloud infrastructure, and containerized applications.
          </p>
          <p class="text-lg text-gray-300">
            I specialize in Infrastructure as Code, Kubernetes orchestration, and cloud-native solutions that help 
            teams ship faster and more reliably.
          </p>
          <div class="flex flex-wrap gap-4">
            <div class="bg-gray-800 px-5 py-3 rounded-xl">🇮🇳 Bengaluru, India</div>
            <div class="bg-gray-800 px-5 py-3 rounded-xl">Open to opportunities</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Skills -->
  <section id="skills" class="py-20">
    <div class="max-w-6xl mx-auto px-6">
      <h2 class="text-4xl font-bold text-center mb-12">Skills & Technologies</h2>
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        <div class="bg-gray-800 p-6 rounded-2xl card-hover text-center">
          <i class="fab fa-docker text-5xl text-blue-500 mb-4"></i>
          <h3 class="text-xl font-semibold">Docker</h3>
        </div>
        <div class="bg-gray-800 p-6 rounded-2xl card-hover text-center">
          <i class="fas fa-dharmachakra text-5xl text-blue-600 mb-4"></i>
          <h3 class="text-xl font-semibold">Kubernetes</h3>
        </div>
        <div class="bg-gray-800 p-6 rounded-2xl card-hover text-center">
          <i class="fab fa-aws text-5xl text-orange-500 mb-4"></i>
          <h3 class="text-xl font-semibold">AWS</h3>
        </div>
        <div class="bg-gray-800 p-6 rounded-2xl card-hover text-center">
          <i class="fab fa-github text-5xl mb-4"></i>
          <h3 class="text-xl font-semibold">GitHub Actions</h3>
        </div>
        <div class="bg-gray-800 p-6 rounded-2xl card-hover text-center">
          <span class="text-5xl mb-4 block">☁️</span>
          <h3 class="text-xl font-semibold">Terraform</h3>
        </div>
        <div class="bg-gray-800 p-6 rounded-2xl card-hover text-center">
          <i class="fas fa-server text-5xl text-emerald-500 mb-4"></i>
          <h3 class="text-xl font-semibold">Linux</h3>
        </div>
        <div class="bg-gray-800 p-6 rounded-2xl card-hover text-center">
          <span class="text-5xl mb-4 block">🐙</span>
          <h3 class="text-xl font-semibold">Jenkins</h3>
        </div>
        <div class="bg-gray-800 p-6 rounded-2xl card-hover text-center">
          <i class="fas fa-shield-alt text-5xl text-purple-500 mb-4"></i>
          <h3 class="text-xl font-semibold">Monitoring</h3>
        </div>
      </div>
    </div>
  </section>

  <!-- Projects -->
  <section id="projects" class="py-20 bg-gray-900">
    <div class="max-w-6xl mx-auto px-6">
      <h2 class="text-4xl font-bold text-center mb-12">Featured Projects</h2>
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- Project 1 -->
        <div class="bg-gray-800 rounded-3xl overflow-hidden card-hover">
          <div class="h-48 bg-gradient-to-r from-blue-600 to-cyan-500 flex items-center justify-center">
            <span class="text-6xl">☸️</span>
          </div>
          <div class="p-6">
            <h3 class="text-2xl font-bold mb-2">E-commerce Platform on Kubernetes</h3>
            <p class="text-gray-400 mb-4">Deployed a highly available microservices e-commerce app using Helm charts and GitOps.</p>
            <div class="flex gap-2 flex-wrap">
              <span class="text-xs bg-gray-700 px-3 py-1 rounded-full">Kubernetes</span>
              <span class="text-xs bg-gray-700 px-3 py-1 rounded-full">ArgoCD</span>
              <span class="text-xs bg-gray-700 px-3 py-1 rounded-full">AWS EKS</span>
            </div>
          </div>
        </div>

        <!-- Project 2 -->
        <div class="bg-gray-800 rounded-3xl overflow-hidden card-hover">
          <div class="h-48 bg-gradient-to-r from-orange-500 to-red-500 flex items-center justify-center">
            <span class="text-6xl">🚀</span>
          </div>
          <div class="p-6">
            <h3 class="text-2xl font-bold mb-2">CI/CD Pipeline Automation</h3>
            <p class="text-gray-400 mb-4">Reduced deployment time by 85% with a complete GitHub Actions + Terraform pipeline.</p>
            <div class="flex gap-2 flex-wrap">
              <span class="text-xs bg-gray-700 px-3 py-1 rounded-full">Terraform</span>
              <span class="text-xs bg-gray-700 px-3 py-1 rounded-full">GitHub Actions</span>
              <span class="text-xs bg-gray-700 px-3 py-1 rounded-full">Docker</span>
            </div>
          </div>
        </div>

        <!-- Project 3 -->
        <div class="bg-gray-800 rounded-3xl overflow-hidden card-hover">
          <div class="h-48 bg-gradient-to-r from-purple-600 to-pink-500 flex items-center justify-center">
            <span class="text-6xl">📊</span>
          </div>
          <div class="p-6">
            <h3 class="text-2xl font-bold mb-2">Monitoring Dashboard</h3>
            <p class="text-gray-400 mb-4">Built centralized observability platform using Prometheus, Grafana & Loki.</p>
            <div class="flex gap-2 flex-wrap">
              <span class="text-xs bg-gray-700 px-3 py-1 rounded-full">Prometheus</span>
              <span class="text-xs bg-gray-700 px-3 py-1 rounded-full">Grafana</span>
              <span class="text-xs bg-gray-700 px-3 py-1 rounded-full">ELK</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact -->
  <section id="contact" class="py-20">
    <div class="max-w-4xl mx-auto px-6">
      <h2 class="text-4xl font-bold text-center mb-12">Let's Connect</h2>
      <div class="bg-gray-800 rounded-3xl p-10">
        <form class="space-y-6">
          <div class="grid md:grid-cols-2 gap-6">
            <input type="text" placeholder="Your Name" 
                   class="bg-gray-900 border border-gray-700 rounded-2xl px-6 py-4 focus:outline-none focus:border-emerald-500">
            <input type="email" placeholder="Email Address" 
                   class="bg-gray-900 border border-gray-700 rounded-2xl px-6 py-4 focus:outline-none focus:border-emerald-500">
          </div>
          <input type="text" placeholder="Subject" 
                 class="w-full bg-gray-900 border border-gray-700 rounded-2xl px-6 py-4 focus:outline-none focus:border-emerald-500">
          <textarea placeholder="Your Message" rows="6"
                    class="w-full bg-gray-900 border border-gray-700 rounded-2xl px-6 py-4 focus:outline-none focus:border-emerald-500"></textarea>
          <button type="submit"
                  class="w-full bg-emerald-600 hover:bg-emerald-500 py-5 rounded-2xl font-semibold text-lg transition">
            Send Message
          </button>
        </form>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-black py-12 border-t border-gray-800">
    <div class="max-w-6xl mx-auto px-6 text-center">
      <p class="text-gray-500">© 2026 Rakesh. Built with ❤️ for DevOps</p>
    </div>
  </footer>

  <script>
    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        if (this.getAttribute('href') !== '#') {
          e.preventDefault();
          document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
          });
        }
      });
    });

    // Simple form submission alert
    document.querySelector('form').addEventListener('submit', function(e) {
      e.preventDefault();
      alert("Thank you! Your message has been received. (Demo)");
    });
  </script>
</body>
</html>