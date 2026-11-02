---
records:
    - id: MK2FXP0WTF
      kind: monograph
      title: Groups of Cohomological Dimension One
      creators:
        - name: Daniel E. Cohen
          role: author
      date: "1972"
      msc:
        - code: 20J05
          from: zbmath_search
        - code: 20-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1972"
          ids:
            doi: 10.1007/bfb0069645
            zbl: "0231.20018"
            zbl_id: "3365504"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1972"
              ids:
                isbn:
                    - "9783540057598"
                    - "9783540371809"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0069645
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3365504"
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
    - id: MK2K1M1F06
      kind: course
      title: Approximate Reasoning using Fuzzy Set Theory
      creators:
        - name: Balasubramaniam Jayaram
          role: instructor
      date: "2022-08-16"
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2022-08-16"
          structure: MK2K1M1F06/e1.json
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Hyderabad
              ids:
                nptel: "111106162"
              access:
                class: record
            - key: m2
              kind: page
              date: "2022-08-16"
              ids:
                nptel: "111106162"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 dev scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111106162"
          level: manifestation
        - source: nptel_video
          snapshot: blake3:7980ec84cfbca0f71922ec2d4e56d2385fa22a44c9cd025088eefbf06b61009d
          native_id: "111106162"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
---
