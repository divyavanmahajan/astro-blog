import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
	type: 'content',
	// Type-check frontmatter using a schema
	schema: z.object({
		title: z.string(),
		description: z.string(),
		// Transform string to Date object
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		heroImage: z.string().optional(),
		categories: z.array(z.string()).default(['General']),
		tags: z.array(z.string()).default([]),
		draft: z.boolean().default(false),
		author: z.string().optional(),
		linkedin: z.boolean().default(false),
		linkedinMessage: z.string().optional(),
		linkedinArticleUrl: z.string().optional(),
		series: z.string().optional(), // Format: "series-name-001"
	}),
});

// TIL (Today I Learned) collection - simpler schema for quick notes
const til = defineCollection({
	type: 'content',
	schema: z.object({
		title: z.string(),
		description: z.string(),
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		tags: z.array(z.string()),
		draft: z.boolean().default(false),
	}),
});

export const collections = { blog, til };
