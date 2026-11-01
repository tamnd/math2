---
records:
    - id: CTQBZ92HYT
      kind: monograph
      title: Random Fields
      creators:
        - name: Chris Preston
          role: author
      date: "1976"
      msc:
        - code: 60K35
          from: zbmath_search
        - code: 60G20
          from: zbmath_search
        - code: 60-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1976"
          ids:
            doi: 10.1007/bfb0080563
            zbl: "0335.60074"
            zbl_id: "3524558"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540078524"
                    - "9783540381938"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0080563
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3524558"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: CTQDSD0HAD
      kind: preprint
      title: A Fast and Stable Square-Root-Free Unitary Core-Chasing Algorithm
      creators:
        - name: Mónica Esquivel-Rosado
          role: author
        - name: Jared L. Aurentz
          role: author
        - name: Giovanni Barbarino
          role: author
        - name: María C. Quintana
          role: author
      date: "2026-10-08"
      msc:
        - code: 65-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.NA
        - system: arxiv
          code: cs.NA
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-08"
          ids:
            arxiv: "2610.12228"
            zbl_id: "903204774"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.12228"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.12228"
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "903204774"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
