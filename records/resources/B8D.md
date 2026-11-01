---
records:
    - id: B8D26BYA7T
      kind: preprint
      title: Proof of the Kahn Saks Conjecture
      creators:
        - name: Max Aires
          role: author
      date: "2026-09-25"
      msc:
        - code: 05-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.CO
        - system: arxiv
          code: cs.DM
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-09-25"
          ids:
            arxiv: "2609.30895"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.30895"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2609.30895"
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
    - id: B8DXQ8K1J7
      kind: monograph
      title: Harmonic Maps Between Surfaces (with a Special Chapter on Conformal Mappings)
      creators:
        - name: Jürgen Jost
          role: author
      date: "1984"
      msc:
        - code: "58E20"
          from: zbmath_search
        - code: 58J32
          from: zbmath_search
        - code: 58-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1984"
          ids:
            doi: 10.1007/bfb0100160
            zbl: "0542.58002"
            zbl_id: "3862078"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1984"
              ids:
                isbn:
                    - "9783540133391"
                    - "9783540388685"
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
          native_id: 10.1007/bfb0100160
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3862078"
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
---
