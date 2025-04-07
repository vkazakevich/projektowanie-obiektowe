<?php

namespace App\DataFixtures;

use App\Entity\Product;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;

class AppFixtures extends Fixture
{
    public function load(ObjectManager $manager): void
    {
        for ($i = 0; $i < 20; $i++) {
            $product = new Product();

            $product->setName('product '.$i);
            $product->setPrice(mt_rand(10, 100));
            $product->setQuantity(mt_rand(0, 1000));
            $manager->persist($product);
        }

        $manager->flush();
    }
}
