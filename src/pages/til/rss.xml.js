import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
    const tils = (await getCollection('til'))
        .filter((til) => !til.data.draft)
        .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());

    const site = context.site || 'https://divyavanmahajan.github.io';

    return rss({
        title: 'TIL - Things I\'ve Learned',
        description: 'Quick notes about things I\'ve learned',
        site: site,
        items: tils.map((til) => ({
            title: til.data.title,
            pubDate: til.data.pubDate,
            description: til.data.description,
            link: `${import.meta.env.BASE_URL}til/${til.slug}/`,
        })),
        customData: `<language>en-us</language>`,
    });
}
