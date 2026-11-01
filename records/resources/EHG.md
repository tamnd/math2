---
records:
    - id: EHGC66YK3Y
      kind: problem-set
      title: Putnam 2003
      creators:
        - name: Mathematical Association of America
          role: author
      date: "2003"
      msc:
        - code: 00A07
          from: putnam
        - code: 97U40
          from: putnam
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2003"
          structure: EHGC66YK3Y/e1.json
      relations:
        - kind: part_of
          to: TYDZDDC2MA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: putnam
          snapshot: blake3:a8efce689e279311a280a90aaaac925d4b96f7c8ccdd9eb1e8fb29b48d574603
          native_id: "2003"
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
    - id: EHGJX4ETBN
      kind: preprint
      title: Petrov-Galerkin operator inference with application to stability-encouraging identification
      creators:
        - name: Johannes Rettberg
          role: author
        - name: Jonas Nicodemus
          role: author
        - name: Harsh Sharma
          role: author
        - name: Boris Kramer
          role: author
        - name: Jörg Fehr
          role: author
        - name: Benjamin Unger
          role: author
      date: "2026-10-01"
      msc:
        - code: 49-XX
          from: arxiv
        - code: 90-XX
          from: arxiv
        - code: 93-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.OC
        - system: arxiv
          code: cs.SY
        - system: arxiv
          code: eess.SY
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-01"
          ids:
            arxiv: "2610.01295"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.01295"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.01295"
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
    - id: EHGM9HPNA5
      kind: monograph
      title: Aspects of Constructibility
      creators:
        - name: Keith J. Devlin
          role: author
      date: "1973"
      msc:
        - code: "03E15"
          from: zbmath_search
        - code: "03E55"
          from: zbmath_search
        - code: 03-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1973"
          ids:
            doi: 10.1007/bfb0059290
            zbl: "0312.02054"
            zbl_id: "3487448"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1973"
              ids:
                isbn:
                    - "9783540065227"
                    - "9783540378211"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0059290
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3487448"
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
