---
records:
    - id: ZEHGD7EHGH
      kind: monograph
      title: Microlocal Analysis and Applications
      creators:
        - name: Jean Michel Bony
          role: author
        - name: Gerd Grubb
          role: author
        - name: Lars Hörmander
          role: author
        - name: Hikosaburo Komatsu
          role: author
        - name: Johannes Sjöstrand
          role: author
        - name: Lamberto Cattabriga
          role: editor
        - name: Luigi Rodino
          role: editor
      date: "1991"
      expressions:
        - key: e1
          kind: edition
          date: "1991"
          ids:
            doi: 10.1007/bfb0085120
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1991"
              ids:
                isbn:
                    - "9783540549482"
                    - "9783540466031"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0085120
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: ZEHQDJTEDG
      kind: preprint
      title: Unique continuation for the periodic Benjamin-Bona-Mahony equation
      creators:
        - name: Roberto de A. Capistrano Filho
          role: author
        - name: Victor Hugo Gonzalez Martinez
          role: author
        - name: Ailton Campos do Nascimento
          role: author
      date: "2026-09-28"
      msc:
        - code: 35-XX
          from: arxiv
        - code: 49-XX
          from: arxiv
        - code: 90-XX
          from: arxiv
        - code: 93-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.AP
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-09-28"
          ids:
            arxiv: "2609.36204"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.36204"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2609.36204"
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
