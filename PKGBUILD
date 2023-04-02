# Maintainer: Firas Chaib <firas1120@gmail.com>
pkgname=ssrfhunter
pkgver=1.1
pkgrel=1
pkgdesc="A simple tool that tests for potential SSRF vulnerability"
arch=('any')
url="https://github.com/not1cyyy/SSRFHunter"
license=('GPL-3.0')
depends=('python' 'python-requests')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -Dm755 ssrfhunter.py "${pkgdir}/usr/bin/ssrfhunter"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

md5sums=('a5e39de54d65b87a1119e24c7b6eefa4')