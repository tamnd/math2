---
records:
    - id: YYC3BF9439
      kind: problem-set
      title: IMO 2023 Shortlist
      creators:
        - name: IMO Problem Selection Committee
          role: author
      date: "2023"
      msc:
        - code: 00A07
          from: imo
        - code: 97U40
          from: imo
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2023"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: 2023-sl
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from deferred to in
    - id: YYCNVSWKC4
      kind: monograph
      title: A Course in Minimal Surfaces
      creators:
        - name: Tobias Colding
          role: author
        - name: William Minicozzi
          role: author
      date: "2011-04-01"
      msc:
        - code: 53A10
          from: zbmath_search
        - code: 53C42
          from: zbmath_search
        - code: "58E12"
          from: zbmath_search
        - code: 49Q05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2011-04-01"
          ids:
            doi: 10.1090/gsm/121
            zbl: "1242.53007"
            zbl_id: "5881490"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2011-04-01"
              ids:
                isbn:
                    - "9780821853238"
                    - "9780821884232"
                    - "9781470411824"
              access:
                class: record
      relations:
        - kind: part_of
          to: YBEDX3XNVA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/gsm/121
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "5881490"
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
